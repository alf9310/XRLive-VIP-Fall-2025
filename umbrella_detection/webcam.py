import cv2 as cv
import numpy as np
import pytorch as torch

cam = cv.VideoCapture()

frame_w = int(cam.get(cv.CAP_PROP_FRAME_WIDTH))
frame_h = int(cam.get(cv.CAP_PROP_FRAME_HEIGHT))

fourcc = cv.VideoWriter_fourcc(*'mp4v')
out = cv.VideoWriter('output.mp4', fourcc, 20.0, (frame_w, frame_h))

while True:
    ret, frame = cam.read()

    out.write(frame)
    cv.imshow('Camera', frame)

    if cv.waitKey(1) == ord('q'):
        break

cam.release()
out.release()
cv.destroyAllWindows()