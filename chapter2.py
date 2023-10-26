import cv2
import numpy as np

img=cv2.imread("images/mlimage1.png")
kernel=np.ones((5,5),np.uint8)
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny=cv2.Canny(imgGray,100,100)
imgDialation=cv2.dilate(imgCanny,kernel,iterations=1)
imgEroded=cv2.erode(imgDialation,kernel,iterations=1)


cv2.imshow("Gray image",imgGray)
cv2.imshow("Blur image7",imgBlur)
cv2.imshow("canny image3",imgCanny)
cv2.imshow("Dialation image",imgDialation)
cv2.imshow("Eroded image",imgEroded)


cv2.waitKey(0)