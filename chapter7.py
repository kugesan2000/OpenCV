import cv2

img=cv2.imread("images/img1.jpg")

imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

cv2.imshow("Normal Lamborghini",imgHSV)
cv2.waitKey(0)