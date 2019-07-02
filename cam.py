import cv2
#starting camera
cap=cv2.VideoCapture(2)
tp1=cap.read()[1] #take 1
tp2=cap.read()[1] #take2
tp3=cap.read()[1] #take3
#to make more perfect
gray1=cv2.cvtcolor(tp1,cv2.COLOR_BGR2GRAY) #converting into gray
gray2=cv2.cvtcolor(tp2,cv2.COLOR_BGR2GRAY)
gray3=cv2.cvtcolor(tp3,cv2.COLOR_BGR2GRAY)

#now creatinig image diffrentiater
def img_diff(x,y,z):
    #diff bw x,y---gray1,gray2--d1
    d1=csv2.absdiff(x,y)
    #diff bw y,z---gray2,gray3---d2
    d2=cv2.absdiff(y,z)
    #abs diff d1,d2
    finalimg=cv2.bitwise_and(d1,d2)
    return finalimg
#now apply function
while cap.isOpened():
    status,frame=cap.read() #continue image taker
    motionimg=img_diff(gray1,gray2,gray3)
    #replacig image frame
    gray1=gray2
    gray2=gray3
    gray3=cvv2.color(frame,cv2.COLOR_BG2GRAY) #passing live image to gray3
    cv2.imshow('live',frame)
    cv2.imshow('motion',motionimg)
    cv2.waitkey(10) & 0xff == ord('q') :
        break
cv2.destroyAllWindows()
cap.release()
    
