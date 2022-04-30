import cv2
from matplotlib.pyplot import draw
import mediapipe as mp



mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 255, 255)]
# For webcam input: 
cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4, 720)
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.85,
    min_tracking_confidence=0.85) as hands:
  while cap.isOpened():         #True
        #import image
    success, image = cap.read()
    image = cv2.flip(image,1)
    if not success:
      print("Ignoring empty camera frame.")
      continue

    

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)
    

    # Adding the colour buttons to the live frame for colour access
    image = cv2.rectangle(image, (40,1), (140,65), (122,122,122), -1)
    image = cv2.rectangle(image, (260,1), (360,65), colors[0], -1)
    image = cv2.rectangle(image, (420,1), (520,65), colors[1], -1)
    image = cv2.rectangle(image, (630,1), (730,65), colors[2], -1)
    image = cv2.rectangle(image, (950,1), (1050,65), colors[3], -1)
    cv2.putText(image, "CLEAR ALL", (49, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(image, "BLUE", (285, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(image, "GREEN", (460, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(image, "RED", (650, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(image, "YELLOW", (970, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (150,150,150), 2, cv2.LINE_AA)


    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())
    # Flip the image horizontally for a selfie-view display.
    #image = cv2.resize(image,(224,224))
    cv2.imshow('MediaPipe Hands', image)
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()