import cv2
# ----------
faceCascade= cv2.CascadeClassifier(r"haarcascades/haarcascade_frontalface_default.xml")
Id = 0
cap = cv2.VideoCapture(Id)
cap.set(3, 480) #wigth
cap.set(4,480)  #hight
while True:
    success , img = cap.read()
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray,1.1,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow('Video', img)
    if cv2.waitKey(1)& 0xFF ==ord('q') :
        break

# ----------

# img = cv2.imread('Abdellah ahbar.png')
# imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
 
# faces = faceCascade.detectMultiScale(imgGray,1.1,4)
 
# for (x,y,w,h) in faces:
#     cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
 
# cv2.imshow("Result", img)
# cv2.waitKey(0)