import cv2
import numpy as np
import sys

# Go frame by frame in an mp4 video
if __name__=="__main__":
    video_file = sys.argv[1]
    cap = cv2.VideoCapture(video_file)

    while(cap.isOpened()):
        ret, frame = cap.read()
        if frame is None:
            break

        cv2.imshow('frame', frame)

        if cv2.waitKey(0):
            continue

    cap.release()
    cv2.destroyAllWindows()
