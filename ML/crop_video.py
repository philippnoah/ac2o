import numpy as np
import cv2

cap = cv2.VideoCapture('./archive/video_1.mp4')
bw_sub = cv2.createBackgroundSubtractorMOG2(history=300, varThreshold=40, detectShadows=False)


# Define the codec and create VideoWriter object
img_w, img_h = int(cap.get(3)), int(cap.get(4))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4',fourcc, 20.0, (img_w, img_h))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,0)
        frame = frame[100:300, 150:500]

        bw_frame = bw_sub.apply(frame)
        # bw_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Original", frame)
        cv2.imshow("B&W", bw_frame)

        # write the flipped frame
        out.write(bw_frame)

        # cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
