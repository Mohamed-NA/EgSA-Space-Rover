'''
while True: ultrasonic() --> ultrasonic sensor works all times
if distance <= 0.2:

- rover goes forward for 2 meters(specific number of wheel turns) (calculated by the diameter of the wheel)
- stop and call camera servo function
- servo make its function and call camera to take images

previos steps will be repeated 4 times
if i = 4 : the rover must be at the initial position and has finished the loop
'''

import time

# enable ultra sonic sensor
def enable_ultrasonic()
    while True:
        ultrasonic()
    
    # Obstacle avoidance
    if distance <= 20:
        Right()
        time.sleep(2)

        Left()
        time.sleep(2)

        Left()
        time.sleep(2)

        Right()
        time.sleep(2)




# mapping
def mapping():
    Forward()
    time.sleep(4)

    Right()
    time.sleep(4)

    Right()
    time.sleep(4)

    Right()
    time.sleep(4)