import cv2
import numpy as np

cap = cv2.VideoCapture("./archive/video_1.mp4")

subtractor = cv2.createBackgroundSubtractorMOG2(history=300, varThreshold=15, detectShadows=False)
subtractor2 = cv2.createBackgroundSubtractorMOG2(history=300, varThreshold=20, detectShadows=False)

_, frame = cap.read()

img_w, img_h = int(cap.get(3)), int(cap.get(4))
x,y = img_w/4, img_h/4
h, w = img_w/2, img_h/2

fourcc = cv2.VideoWriter_fourcc(*'MP4V')
out = cv2.VideoWriter('output.mp4', fourcc, 15.0, (img_w,img_h))
# cv2.imwrite("frame%d.jpg" % 1, frame[y:y+h, x:x+w])

while True:
    # read frame
    _, frame = cap.read()

    # save frame to output
    # cropped_frame = frame[y:y+h, x:x+w]
    # color_processed_frame = subtractor2.apply(cropped_frame)
    out.write(frame)

    # apply frmaes
    mask1 = subtractor.apply(frame)
    mask2 = subtractor2.apply(frame)
    # mask3 = cv2.GaussianBlur(mask3, (5,5),0)

    # show frame
    # cv2.imshow("Frame", frame)
    # cv2.imshow("Mask", mask2)

    key = cv2.waitKey(30)
    if key == 27:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
