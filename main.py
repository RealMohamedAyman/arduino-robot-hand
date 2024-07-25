import cv2
import mediapipe as mp
import serial

lastGes = None

# Initialize MediaPipe Hands.
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)

bluetooth_port = 'COM4'
baud_rate = 9600

ser = serial.Serial(bluetooth_port, baud_rate)

def recognize_gesture(landmarks):
    # Extract the required landmarks for the fingers
    thumb_tip = landmarks[mp_hands.HandLandmark.THUMB_TIP]
    index_tip = landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    middle_tip = landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    ring_tip = landmarks[mp_hands.HandLandmark.RING_FINGER_TIP]
    pinky_tip = landmarks[mp_hands.HandLandmark.PINKY_TIP]

    thumb_ip = landmarks[mp_hands.HandLandmark.THUMB_IP]
    index_dip = landmarks[mp_hands.HandLandmark.INDEX_FINGER_DIP]
    middle_pip = landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_PIP]
    ring_pip = landmarks[mp_hands.HandLandmark.RING_FINGER_PIP]
    pinky_pip = landmarks[mp_hands.HandLandmark.PINKY_PIP]

    wrist = landmarks[mp_hands.HandLandmark.WRIST]

    # Calculate if fingers are raised
    is_thumb_up = thumb_tip.y < thumb_ip.y and abs(thumb_tip.x - wrist.x) > abs(thumb_tip.y - wrist.y)
    is_index_up = index_tip.y < index_dip.y
    is_middle_up = middle_tip.y < middle_pip.y
    is_ring_up = ring_tip.y < ring_pip.y
    is_pinky_up = pinky_tip.y < pinky_pip.y

    return f"${int(is_thumb_up)}{int(is_index_up)}{int(is_middle_up)}{int(is_ring_up)}{int(is_pinky_up)}p"
    
# For webcam input:
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, image = cap.read()
    if not success:
        break

    # Flip the image horizontally for a later selfie-view display
    # Convert the BGR image to RGB.
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    image.flags.writeable = False
    results = hands.process(image)

    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            landmarks = hand_landmarks.landmark
            gesture = recognize_gesture(landmarks)
            if not gesture == lastGes:
                ser.write(gesture.encode())
                lastGes = gesture
            cv2.putText(image, gesture, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
    
    # Display the image.
    cv2.imshow('MediaPipe Hands', image)
    if cv2.waitKey(5) & 0xFF == 27:
        break

hands.close()
cap.release()
cv2.destroyAllWindows()
