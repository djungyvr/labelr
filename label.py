import cv2
import numpy as np
import sys
import os
import argparse

# Supports
# - Going frame by frame and labeling a video
# - Generating a file mapping the frame to the label
# - Labeling multiple videos at once, use case, videos of footage in RGB and IR, labeling the RGB frames also labels the IR frames

# Go frame by frame in an mp4 video
if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Labeling videos')
    parser.add_argument('-p', metavar='PREFIX', type=str, help='Prefix matching of videos')
    parser.add_argument('-o', metavar='OUTPUT', type=str, help='Output directory to store result')
    parser.add_argument('-i', metavar='INPUT', type=str, help='Input directory to search')
    args = parser.parse_args()

    prefix_match = args.p
    output_dir = args.o
    input_dir = args.i

    files = [f for f in os.listdir(input_dir) if f.startswith(prefix_match)]

    print('Found the following files:', files)

    caps = [{'fname': f, 'vcap': cv2.VideoCapture(os.path.join(input_dir, f))} for f in files]

    os.mkdir(output_dir)

    with open(os.path.join(output_dir, 'labels'), 'w') as f:
        frame_count = 0
        while(True):
            frames = [{'fname': cap['fname'], 'frame': cap['vcap'].read()} for cap in caps]
            if any([not frame['frame'][0] for frame in frames]):
                break

            # Show all frames that were read successfully
            for frame in frames:
                if frame['frame'][0]:
                    cv2.imshow(frame['fname'], frame['frame'][1])

            # Wait for the input
            k = cv2.waitKey(0)

            # Save all frames
            for frame in frames:
                if frame['frame'][0]:
                    frame_fname = '%s_frame_%06d.jpg' % (frame['fname'], frame_count)
                    frame_path = os.path.join(output_dir, frame_fname)
                    cv2.imwrite(frame_path, frame['frame'][1])
                    f.write('%s,%s\n' % (frame_fname,chr(k)))
            frame_count += 1

    [cap['vcap'].release() for cap in caps]
    cv2.destroyAllWindows()
