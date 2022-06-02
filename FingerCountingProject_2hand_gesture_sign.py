import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=2)

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)

    if len(hands)==1:
        # Hand 1
        print(detector.fingersUp(hands[0]))
        if detector.fingersUp(hands[0])==[0,1,1,0,0]:
            cv2.putText(img,"2",(80,100),cv2.FONT_HERSHEY_COMPLEX,4,(0,0,211),12)
        if detector.fingersUp(hands[0])==[1,1,1,0,0]:
            cv2.putText(img,"3",(80,100),cv2.FONT_HERSHEY_COMPLEX,4,(0,0,211),12)
        if detector.fingersUp(hands[0])==[0,1,1,1,1]:
            cv2.putText(img,"4",(80,100),cv2.FONT_HERSHEY_COMPLEX,4,(0,0,211),12)
        if detector.fingersUp(hands[0])==[1,1,1,1,1]:
            cv2.putText(img,"5",(80,100),cv2.FONT_HERSHEY_COMPLEX,4,(0,0,211),12)
        if detector.fingersUp(hands[0])==[0,1,0,0,0]:
            cv2.putText(img,"1",(80,100),cv2.FONT_HERSHEY_COMPLEX,4,(0,0,211),12)
        if detector.fingersUp(hands[0])==[0,1,1,1,0]:
            cv2.putText(img,"6",(80,100),cv2.FONT_HERSHEY_COMPLEX,4,(0,0,211),12)
        if detector.fingersUp(hands[0])==[0,1,1,0,1]:
            cv2.putText(img,"7",(80,100),cv2.FONT_HERSHEY_COMPLEX,4,(0,0,211),12)
        if detector.fingersUp(hands[0])==[0,1,0,1,1]:
            cv2.putText(img,"8",(80,100),cv2.FONT_HERSHEY_COMPLEX,4,(0,0,211),12)
        if detector.fingersUp(hands[0])==[0,0,1,1,1]:
            cv2.putText(img,"9",(80,100),cv2.FONT_HERSHEY_COMPLEX,4,(0,0,211),12)
        if detector.fingersUp(hands[0])==[1,0,0,0,0]:
            cv2.putText(img,"10",(80,100),cv2.FONT_HERSHEY_COMPLEX,4,(0,0,211),12)
        if detector.fingersUp(hands[0])==[0,0,0,0,0]:
            cv2.putText(img,"0",(80,100),cv2.FONT_HERSHEY_COMPLEX,4,(0,0,211),12)
      




        if len(hands) == 2:
            hand2 = hands[1]
            fingers2 = detector.fingersUp(hand2)
         

    cv2.imshow("Image", img)
    cv2.waitKey(1)
    