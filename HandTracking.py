
import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 2560)  # set new dimensionns to cam object (not cap)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1440)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
pTime = 0
cTime = 0


while True:
     success, img = cap.read()
     imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
     results = hands.process(imgRGB)
     #print(results.multi_hand_landmarks)

     if results.multi_hand_landmarks:
          for handLms in results.multi_hand_landmarks:
               for id , lm in enumerate(handLms.landmark):
                    #print(id, lm)
                    h, w, c= img.shape
                    cx, cy = int(lm.x*w), int(lm.y*h)
                    print(id, cx, cy)
                    if id ==0:
                         cv2.circle(img,(cx, cy),10, (0, 255, 0),cv2.FILLED)


               mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
   #  cTime = time.time()
    #fps = 1/(cTime-pTime)
     #pTime = cTime
     #cv2.putText(img,str(int(fps)),(10,70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)

     scale_percent = 60  # percent of original size

     dim = (1920, 1080)
     resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
     mirrored = cv2.flip(resized, 1)



     cv2.imshow("mirrore", mirrored)
     cv2.waitKey(1)