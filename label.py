import cv2
import numpy as np
import sys
import os

# Go frame by frame in an mp4 video
if __name__=="__main__":
    video_file = sys.argv[1]
    output_dir = sys.argv[2]
    cap = cv2.VideoCapture(video_file)

    os.mkdir(output_dir)


    with open(os.path.join(output_dir, 'labels'), 'w') as f:
        frame_count = 0
        while(cap.isOpened()):
            ret, frame = cap.read()
            if frame is None:
                break

            cv2.imshow('frame', frame)
            k = cv2.waitKey(0)
            frame_fname = str(frame_count) + '.jpg'
            frame_path = os.path.join(output_dir, frame_fname)
            cv2.imwrite(frame_path, frame)
            f.write('%s,%s\n' % (frame_fname,chr(k)))
            frame_count += 1

    cap.release()
    cv2.destroyAllWindows()
