import cv2
import numpy as np

img=np.zeros((512,512,3),np.uint8)
#print(img)
img[:]=154,100,50
#line
cv2.line(img,(0,0),(512,512),(90,155,240),2)
#rectangle
#              startingptendingpt color   thickness or flled   cv2.FILLED
cv2.rectangle(img,(0,0),(250,350),(8,200,6),3)

#circle                            cv2.FILLED
cv2.circle(img,(400,50),30,(255,225,0),2)

#TEXT                    origin      font_style        scale(0.8)  color   thickness(whole no 105)
cv2.putText(img,"OPENCV ",(300,200),cv2.FONT_HERSHEY_DUPLEX,1,(0,255,100),1)

cv2.imshow("output",img)
cv2.waitKey(0)

