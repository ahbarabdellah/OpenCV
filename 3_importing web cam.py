import cv2

Id = 0
cap = cv2.VideoCapture(Id)
cap.set(3, 480) #wigth
cap.set(4,480)  #hight
while True:
    success , img = cap.read()
    cv2.imshow('Video', img)
    if cv2.waitKey(1)& 0xFF ==ord('q') :
        break