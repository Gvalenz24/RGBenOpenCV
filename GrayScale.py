import cv2
import numpy as np
import imutils

bgr = cv2.imread('jack.jpeg')
bgr= imutils.resize(bgr,width=400)
gris = cv2.cvtColor(bgr,cv2.COLOR_BGR2GRAY)

cv2.imshow('Gray', gris)
cv2.waitKey(0)
cv2.destroyAllWindows()