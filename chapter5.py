import cv2
import numpy as np

img=cv2.imread("images/img1.jpg") 

width,height=250,350

pts1=np.float32([[111,219],[287,180],[154,482],[355,440]])
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix=cv2.getPerspectiveTransform(pts1,pts2)
imgoutput=cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("original",img)
cv2.imshow("assigned",imgoutput)

cv2.waitKey(0)