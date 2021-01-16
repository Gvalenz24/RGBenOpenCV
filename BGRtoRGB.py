import cv2
import numpy as np
import imutils

bgr = cv2.imread('prueba.jpg')
bgr= imutils.resize(bgr,width=400)
C1= bgr[:,:,0]
C2= bgr[:,:,1]
C3= bgr[:,:,2]
cv2.imshow('BGR',np.hstack([C1,C2,C3]))

rgb = cv2.cvtColor(bgr,cv2.COLOR_BGR2RGB)
C1= rgb[:,:,0]
C2= rgb[:,:,1]
C3= rgb[:,:,2]
cv2.imshow('RGB',np.hstack([C1,C2,C3]))
cv2.waitKey(0)
cv2.destroyAllWindows()
