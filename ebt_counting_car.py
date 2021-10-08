import cv2
import numpy as np

count = 0

cap1 = cv2.VideoCapture("video2.avi")
background = cv2.createBackgroundSubtractorMOG2()

while True:
    
    ret,frame = cap1.read()
    
    if ret:
        fgmask = background.apply(frame)
        
        cv2.line(frame,(180,540),(1280,540),(0,0,255),2)
        cv2.line(frame,(180,540),(1280,540),(0,0,255),2)
        
        contours,hiearchy = cv2.findContours(fgmask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        
        try:
            hiearchy = hiearchy[0]
        except :
            hiearchy = []
        
        for contour,hier in zip(contours,hiearchy):
            (x,y,w,h) = cv2.boundingRect(contour)
            if w > 170 and h > 170:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2)
                if y > 540:
                    count = count+1
        
        cv2.putText(frame,"car count: "+str(count),(100,200),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),2,cv2.LINE_AA)
        
        cv2.imshow("img",frame)
        
        if cv2.waitKey(1) == 27:
            break

    
cap1.release()
cv2.destroyAllWindows()