import cv2
import time
from PIL import Image

from hands_tracking import HandTrackingDynamic
from robot import *

def main():
    # Variable to track if the robot should start moving
    start_idx = 0

    ctime=0
    ptime=0
    cap = cv2.VideoCapture(0)
    detector = HandTrackingDynamic()

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 600)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)
    
    # Check if the camera is opened
    if not cap.isOpened():
        print("Cannot open camera")
        exit()

    # Initialize the robot
    robot = initialize_robot()

    while True:
        ret, frame = cap.read()
        frame = detector.findFingers(frame)
        detector.findPosition(frame)
        fingers = detector.findFingerUp()

        try:
            movement = detector.check_for_gesture(fingers)
            # Start the robot only when the 'Start' gesture is detected
            if movement == 'Start':
                start_idx = 1

            if start_idx == 1:
                if not movement == "Quit":
                    cv2.putText(frame, movement, (10, 110), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)

                    # Move the robot according to the detected gesture
                    if movement == "Forward":
                        go_forward(robot)
                    elif movement == "Backward":
                        go_backward(robot)
                    elif movement == "Left turn":
                        turn_left(robot)
                    elif movement == "Right turn":
                        turn_right(robot)

                    robot_position = str(robot.pos())
                    cv2.putText(frame, robot_position, (10, 150), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
                    robot_angle = str(robot.heading())
                    cv2.putText(frame, robot_angle, (10, 190), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

                else:
                    save_route(robot)
                    break
        except Exception as e:
            print("Show you hand properly")
            
        ctime = time.time()
        fps = 1 / (ctime - ptime)
        ptime = ctime

        cv2.putText(frame, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
    
        cv2.imshow('Camera', frame)
        # Quit when 'q' is pressed
        if cv2.waitKey(1) == ord('q'):
            break

    # Release everything
    cap.release()
    cv2.destroyAllWindows()


"""
Save the robot's route as an image
"""
def save_route(robot):
    route = robot.getscreen()
    route.getcanvas().postscript(file="robot_route.ps")
    image = Image.open('robot_route.ps')
    image.save('robot_route.png')


if __name__ == "__main__":
    main()