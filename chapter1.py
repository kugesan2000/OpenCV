import cv2
print("package imported")

img= cv2.imread('images/mlimage1.png')
cv2.imshow("output",img)
cv2.waitKey(2000)

'''

cap=cv2.VideoCapture(0)
cap.set(3,640)  #width
cap.set(4,480)  #height
cap.set(10,100)    #brightness

while True:
    sucess,img=cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
'''