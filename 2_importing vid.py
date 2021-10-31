import cv2

path = r'../'
cap = cv2.VideoCapture(path)

while True:
    success , img = cap.read()
    cv2.imshow('Video', img)
    if cv2.waitKey(1)& 0xFF ==ord('q') :
        break