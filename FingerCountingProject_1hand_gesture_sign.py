import cv2 #menambahkan library cv2
from cvzone.HandTrackingModule import HandDetector #menambahkan HandDetector dari cvzone.HandTrackingModule

cap = cv2.VideoCapture(0) #inisialisasi variabel cap
detector = HandDetector(detectionCon=0.8, maxHands=2) #Inisialisasi variabel detector

while True: #kondisi perulangan
    success, img = cap.read() 
    hands, img = detector.findHands(img)

    if len(hands)==1:
        # Hand 1
        print(detector.fingersUp(hands[0]))
        if detector.fingersUp(hands[0])==[0,1,1,0,0]: #kondisi percabangan
            cv2.putText(img,"2",(80,100),cv2.FONT_HERSHEY_COMPLEX,4,(0,0,211),12) #output berupa gambar 2 jika kondisi di atas terpenuhi
        if detector.fingersUp(hands[0])==[1,1,1,0,0]: #kondisi percabangan
            cv2.putText(img,"3",(80,100),cv2.FONT_HERSHEY_COMPLEX,4,(0,0,211),12) #output berupa gambar 3 jika kondisi di atas terpenuhi
        if detector.fingersUp(hands[0])==[0,1,1,1,1]: #kondisi percabangan
            cv2.putText(img,"4",(80,100),cv2.FONT_HERSHEY_COMPLEX,4,(0,0,211),12) #output berupa gambar 4 jika kondisi di atas terpenuhi
        if detector.fingersUp(hands[0])==[1,1,1,1,1]: #kondisi percabangan 
            cv2.putText(img,"5",(80,100),cv2.FONT_HERSHEY_COMPLEX,4,(0,0,211),12) #output berupa gambar 5 jika kondisi di atas terpenuhi
        if detector.fingersUp(hands[0])==[0,1,0,0,0]: #kondisi percabangan 
            cv2.putText(img,"1",(80,100),cv2.FONT_HERSHEY_COMPLEX,4,(0,0,211),12) #output berupa gambar 1 jika kondisi di atas terpenuhi
        if detector.fingersUp(hands[0])==[0,1,1,1,0]: #kondisi percabangan 
            cv2.putText(img,"6",(80,100),cv2.FONT_HERSHEY_COMPLEX,4,(0,0,211),12) #output berupa gambar 6 jika kondisi di atas terpenuhi
        if detector.fingersUp(hands[0])==[0,1,1,0,1]: #kondisi percabangan
            cv2.putText(img,"7",(80,100),cv2.FONT_HERSHEY_COMPLEX,4,(0,0,211),12) #output berupa gambar 7 jika kondisi di atas terpenuhi
        if detector.fingersUp(hands[0])==[0,1,0,1,1]: #kondisi percabangan 
            cv2.putText(img,"8",(80,100),cv2.FONT_HERSHEY_COMPLEX,4,(0,0,211),12) #output berupa gambar 8 jika kondisi di atas terpenuhi
        if detector.fingersUp(hands[0])==[0,0,1,1,1]: #kondisi percabangan
            cv2.putText(img,"9",(80,100),cv2.FONT_HERSHEY_COMPLEX,4,(0,0,211),12) #output berupa gambar 9 jika kondisi di atas terpenuhi
        if detector.fingersUp(hands[0])==[1,0,0,0,0]: #kondisi percabangan
            cv2.putText(img,"10",(80,100),cv2.FONT_HERSHEY_COMPLEX,4,(0,0,211),12) #output berupa gambar 10 jika kondisi di atas terpenuhi
        if detector.fingersUp(hands[0])==[0,0,0,0,0]: #kondisi percabangan 
            cv2.putText(img,"0",(80,100),cv2.FONT_HERSHEY_COMPLEX,4,(0,0,211),12) #output berupa gambar 0 jika kondisi di atas terpenuhi
      



        #hands2
        if len(hands) == 2:
            hand2 = hands[1] #inisialisasi variabel hand2 berupa nilai index pertama array hands
            fingers2 = detector.fingersUp(hand2) #inisialisasi variabel fingers2 
         

    cv2.imshow("Image", img)
    cv2.waitKey(1)
    
