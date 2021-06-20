import mediapipe as mp
from cv2 import cv2 as cv2

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
cap = cv2.VideoCapture(0)

tips = {"thumb": 4,
        "index": 8,
        "middle": 12,
        "ring": 16,
        "little": 20}

def fingers_raised(fingers):
    return [fingers[4][1] < fingers[3][1], #true if thumb is open
            fingers[8][2] < fingers[6][2], #true if index is open
            fingers[12][2] < fingers[10][2], #true if middle finger is open
            fingers[16][2] < fingers[14][2], #true if ring finger is open
            fingers[20][2] < fingers[18][2] #true if little finger is open
            ]

    
def main():
    with mp_hands.Hands(
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7) as hands:

        binary_mode = True
        while cap.isOpened():
            cpt = 0
            _, image = cap.read()
            image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            results = hands.process(image)
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            
            res_right = []

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(
                        image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                height, width, _ = image.shape
                right_hand = results.multi_hand_landmarks[0]


                # Position of all the joints in the hand
                for i, lm in enumerate(right_hand.landmark):
                    res_right.append((i, lm.x * height, lm.y * width))
                
                
                fingers_open_right = fingers_raised(res_right)

                if not binary_mode:
                    cpt = sum(fingers_open_right)
                else:
                    for i, digit in enumerate(fingers_open_right):
                        if digit:
                            cpt += 2 ** i
                    


                cv2.rectangle(image, (0, 350), (100, 450), (0, 255, 0), cv2.FILLED)
                cv2.putText(image, str(cpt), (40, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3)
            cv2.putText(image, "Binary mode" if binary_mode else "Decimal mode", (0, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3)

            cv2.imshow('Finger counting', image)
            if cv2.waitKey(5) & 0xFF == 32:
                binary_mode = not binary_mode
            
            if cv2.waitKey(5) & 0xFF == 27:
                break
            
        cap.release()

if __name__ == '__main__':
    main()