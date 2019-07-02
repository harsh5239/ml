import cv2
#calling classifirer
casclf=cv2.CascadeClassifier('face.xml')
#loading face data
cap=cv2.videocapture(2)
while cap.isOpened():
    status,frame=cap.read()
    #applying classifier in live frame
    face=casclf.detectMultiscale(frame,1.13,5) #classifier turning paramete
   # print(face)
    for x,y,h,w in face:
        cv2.rectangle(frame,(x,y),(x+h,y+w),(0,0,255),2)
        #onlyface
        #facedata=frame[x:x+h,y:y+w]
        #cv2.imshow('f',facedata)
    cv2.imshow('face',frame)
    if cv2.waitkey(10) &0xff == ord('q') :
        break
    

cv2.destroyAllWindows()
cap.release()
