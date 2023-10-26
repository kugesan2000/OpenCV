import cv2
import numpy as np

img=cv2.imread("images/img1.jpg")
print(img.shape)
imgresize=cv2.resize(img,(300,400))

imgcropped=img[30:100,50:120]

cv2.imshow("imgbeforeresize",img)
cv2.imshow("imgafteresize",imgresize)
cv2.imshow("imgcropped",imgcropped)

print(imgresize.shape)
cv2.waitKey(0)