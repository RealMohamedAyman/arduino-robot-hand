# Arduino Robot Hand

This project is an Arduino-powered robot hand that mimics hand gestures detected by a camera in real time. The camera captures the hand gestures, which are then processed using MediaPipe and sent to the Arduino via serial communication to control the servos on the robot hand.

## Features

- Real-time hand gesture recognition using MediaPipe
- Serial communication between the Python script and Arduino
- Control of individual fingers on the robot hand using servos

## Requirements

### Hardware

- Arduino board (e.g., Arduino Uno)
- 5 Servo motors
- Camera (e.g., a webcam)

### Software

- Python 3.x
- OpenCV
- MediaPipe
- PySerial
- Arduino IDE

## Setup

### Arduino

1. Connect the servos to the Arduino board:
    - Thumb: Pin 6
    - Index: Pin 5
    - Middle: Pin 4
    - Ring: Pin 3
    - Pinky: Pin 2
2. Upload the Arduino code to the Arduino board using the Arduino IDE.

### Python

1. Install the required Python libraries:

    ```bash
    pip install opencv-python mediapipe pyserial
    ```

2. Save the Python script.

## Running the Project

1. Connect the Arduino to your computer and upload the Arduino code.
2. Run the Python script:

    ```bash
    python your_script_name.py
    ```

3. Make sure the webcam is enabled and capturing your hand gestures.
4. The robot hand should now mimic your hand gestures in real-time.
