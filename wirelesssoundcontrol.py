import cv2
import mediapipe as mp
from sympy import re

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

cap = cv2.VideoCapture(0)

while True:
    success, image = cap.read()
    image = cv2.cvtcolor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            lmList=[]
            for id, lm in enumerate(handLms.landmarks):
                #print(id,lm)
                h, w, c = image.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                #print(id,cx,cy)
                lmList.append([id,cx,cy])
                print(lmList)


            #mp_drawing.draw_landmarks(image, handLms, mp_hands.HAND_CONNECTIONS)
    cv2.imshow("Hand",image)
    cv2.waitkey(1)


