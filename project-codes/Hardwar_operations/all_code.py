import time
from turtle import left
import RPi.GPIO as GPIO
from i2c_hmc5883l import HMC5883
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

count = 0


# =====================
# -- PINs Definition --
# =====================
# Motor PINS
# 3 Drivers
# Frist Driver - Right
Driver_1_Right_IN1 = 5
Driver_1_Right_IN2 = 6
Driver_1_Right_IN3 = 23
Driver_1_Right_IN4 = 25
Driver_1_Right_ENA = 12 #PWM
Driver_1_Right_ENB = 12 #PWM

# 2nd Driver - Left
Driver_2_Left_IN1 = 22
Driver_2_Left_IN2 = 27
Driver_2_Left_IN3 = 4 
Driver_2_Left_IN4 = 24
Driver_2_Left_ENA = 13 #PWM
Driver_2_Left_ENB = 13 #PWM

# 3rd Driver
Driver_3_LastRL_IN1 = 21 # Right one back
Driver_3_LastRL_IN2 = 26 # Right one back   
Driver_3_LastRL_IN3 = 17 # Left one back
Driver_3_LastRL_IN4 = 20 # Left one back
Driver_3_LastRL_ENA = 18 # PWM
Driver_3_LastRL_ENB = 18 # PWM

# ---------------------------
# ultra sonic PINS
TRIG = 23
ECHO = 24
# ---------------------------
# camera PINS
servoPIN = 18



# ================
# -- PINS Setup --
# ================
# pins for motors
# 1st Driver - Right
GPIO.setup(Driver_1_Right_IN1, GPIO.OUT)
GPIO.setup(Driver_1_Right_IN2, GPIO.OUT)
GPIO.setup(Driver_1_Right_IN3, GPIO.OUT)
GPIO.setup(Driver_1_Right_IN4, GPIO.OUT)
GPIO.setup(Driver_1_Right_ENA, GPIO.OUT)
GPIO.setup(Driver_1_Right_ENB, GPIO.OUT)

D_R_ENA = GPIO.PWM(Driver_1_Right_ENA, 50)
D_R_ENB = GPIO.PWM(Driver_1_Right_ENB, 50)


# 2nd Driver - Left
GPIO.setup(Driver_2_Left_IN1, GPIO.OUT)
GPIO.setup(Driver_2_Left_IN2, GPIO.OUT)
GPIO.setup(Driver_2_Left_IN3, GPIO.OUT)
GPIO.setup(Driver_2_Left_IN4, GPIO.OUT)
GPIO.setup(Driver_2_Left_ENA, GPIO.OUT)
GPIO.setup(Driver_2_Left_ENB, GPIO.OUT)

D_L_ENA = GPIO.PWM(Driver_2_Left_ENA, 50)
D_L_ENB = GPIO.PWM(Driver_2_Left_ENB, 50)


# 3rd Driver - Last Reverse 
# 2nd Driver - Left
GPIO.setup(Driver_3_LastRL_IN1, GPIO.OUT)
GPIO.setup(Driver_3_LastRL_IN2, GPIO.OUT)
GPIO.setup(Driver_3_LastRL_IN3, GPIO.OUT)
GPIO.setup(Driver_3_LastRL_IN4, GPIO.OUT)
GPIO.setup(Driver_3_LastRL_ENA, GPIO.OUT)
GPIO.setup(Driver_3_LastRL_ENB, GPIO.OUT)

D_RL_ENA = GPIO.PWM(Driver_3_LastRL_ENA, 50)
D_RL_ENB = GPIO.PWM(Driver_3_LastRL_ENB, 50)

# MACROS
Max_Speed = 90

# ---------------------------
# pins for ultra sonic
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
# ---------------------------
# pins for camera
GPIO.setup(servoPIN, GPIO.OUT)



# ===============
# -- FUNCTIONS --
# ===============
# Movement Functions for motors

def forward():
    #Bringing All to Stop
    D_R_ENA.start(0)
    D_R_ENB.start(0)
    D_L_ENA.start(0)
    D_RL_ENA.start(0)
    D_RL_ENB.start(0)
    time.sleep(1)

    #Setting Up Directions
    GPIO.output(Driver_1_Right_IN1, GPIO.HIGH)
    GPIO.output(Driver_1_Right_IN2, GPIO.LOW)
    GPIO.output(Driver_1_Right_IN3, GPIO.HIGH)
    GPIO.output(Driver_1_Right_IN4, GPIO.LOW)

    GPIO.output(Driver_2_Left_IN1, GPIO.HIGH)
    GPIO.output(Driver_2_Left_IN2, GPIO.LOW)
    GPIO.output(Driver_2_Left_IN3, GPIO.HIGH)
    GPIO.output(Driver_2_Left_IN4, GPIO.LOW)

    GPIO.output(Driver_3_LastRL_IN1, GPIO.HIGH)
    GPIO.output(Driver_3_LastRL_IN2, GPIO.LOW)
    GPIO.output(Driver_3_LastRL_IN3, GPIO.HIGH)
    GPIO.output(Driver_3_LastRL_IN4, GPIO.LOW)


    # Change Motor Speeds to Higher
    D_R_ENA.ChangeDutyCycle(Max_Speed)
    D_R_ENB.ChangeDutyCycle(Max_Speed)
    D_L_ENA.ChangeDutyCycle(Max_Speed)
    D_L_ENB.ChangeDutyCycle(Max_Speed)
    D_RL_ENA.ChangeDutyCycle(Max_Speed)
    D_RL_ENB.ChangeDutyCycle(Max_Speed)


def backward():
    #Bringing All to Stop
    D_R_ENA.start(0)
    D_R_ENB.start(0)
    D_L_ENA.start(0)
    D_RL_ENA.start(0)
    D_RL_ENB.start(0)
    time.sleep(1)

    #Setting Up Directions
    GPIO.output(Driver_1_Right_IN1, GPIO.LOW)
    GPIO.output(Driver_1_Right_IN2, GPIO.HIGH)
    GPIO.output(Driver_1_Right_IN3, GPIO.LOW)
    GPIO.output(Driver_1_Right_IN4, GPIO.HIGH)

    GPIO.output(Driver_2_Left_IN1, GPIO.LOW)
    GPIO.output(Driver_2_Left_IN2, GPIO.HIGH)
    GPIO.output(Driver_2_Left_IN3, GPIO.LOW)
    GPIO.output(Driver_2_Left_IN4, GPIO.HIGH)

    GPIO.output(Driver_3_LastRL_IN1, GPIO.LOW)
    GPIO.output(Driver_3_LastRL_IN2, GPIO.HIGH)
    GPIO.output(Driver_3_LastRL_IN3, GPIO.LOW)
    GPIO.output(Driver_3_LastRL_IN4, GPIO.HIGH)


    # Change Motor Speeds to Higher
    D_R_ENA.ChangeDutyCycle(Max_Speed)
    D_R_ENB.ChangeDutyCycle(Max_Speed)
    D_L_ENA.ChangeDutyCycle(Max_Speed)
    D_L_ENB.ChangeDutyCycle(Max_Speed)
    D_RL_ENA.ChangeDutyCycle(Max_Speed)
    D_RL_ENB.ChangeDutyCycle(Max_Speed)


def right():
    #Bringing All to Stop
    D_R_ENA.start(0)
    D_R_ENB.start(0)
    D_L_ENA.start(0)
    D_RL_ENA.start(0)
    D_RL_ENB.start(0)
    time.sleep(1)

    #Setting Up Directions
    GPIO.output(Driver_1_Right_IN1, GPIO.LOW)
    GPIO.output(Driver_1_Right_IN2, GPIO.HIGH)
    GPIO.output(Driver_1_Right_IN3, GPIO.LOW)
    GPIO.output(Driver_1_Right_IN4, GPIO.HIGH)

    GPIO.output(Driver_2_Left_IN1, GPIO.HIGH)
    GPIO.output(Driver_2_Left_IN2, GPIO.LOW)
    GPIO.output(Driver_2_Left_IN3, GPIO.HIGH)
    GPIO.output(Driver_2_Left_IN4, GPIO.LOW)

    GPIO.output(Driver_3_LastRL_IN1, GPIO.LOW)
    GPIO.output(Driver_3_LastRL_IN2, GPIO.HIGH)
    GPIO.output(Driver_3_LastRL_IN3, GPIO.HIGH)
    GPIO.output(Driver_3_LastRL_IN4, GPIO.LOW)


    # Change Motor Speeds to Higher
    D_R_ENA.ChangeDutyCycle(Max_Speed)
    D_R_ENB.ChangeDutyCycle(Max_Speed)
    D_L_ENA.ChangeDutyCycle(Max_Speed)
    D_L_ENB.ChangeDutyCycle(Max_Speed)
    D_RL_ENA.ChangeDutyCycle(Max_Speed)
    D_RL_ENB.ChangeDutyCycle(Max_Speed)


def Left():
    #Bringing All to Stop
    D_R_ENA.start(0)
    D_R_ENB.start(0)
    D_L_ENA.start(0)
    D_RL_ENA.start(0)
    D_RL_ENB.start(0)
    time.sleep(1)

    #Setting Up Directions
    GPIO.output(Driver_1_Right_IN1, GPIO.HIGH)
    GPIO.output(Driver_1_Right_IN2, GPIO.LOW)
    GPIO.output(Driver_1_Right_IN3, GPIO.HIGH)
    GPIO.output(Driver_1_Right_IN4, GPIO.LOW)

    GPIO.output(Driver_2_Left_IN1, GPIO.LOW)
    GPIO.output(Driver_2_Left_IN2, GPIO.HIGH)
    GPIO.output(Driver_2_Left_IN3, GPIO.LOW)
    GPIO.output(Driver_2_Left_IN4, GPIO.HIGH)

    GPIO.output(Driver_3_LastRL_IN1, GPIO.HIGH)
    GPIO.output(Driver_3_LastRL_IN2, GPIO.LOW)
    GPIO.output(Driver_3_LastRL_IN3, GPIO.LOW)
    GPIO.output(Driver_3_LastRL_IN4, GPIO.HIGH)


    # Change Motor Speeds to Higher
    D_R_ENA.ChangeDutyCycle(Max_Speed)
    D_R_ENB.ChangeDutyCycle(Max_Speed)
    D_L_ENA.ChangeDutyCycle(Max_Speed)
    D_L_ENB.ChangeDutyCycle(Max_Speed)
    D_RL_ENA.ChangeDutyCycle(Max_Speed)
    D_RL_ENB.ChangeDutyCycle(Max_Speed)




# functions for sensors
def ultra_sonic():
    # setting TRIG pin
    # stop for 0.1 sec
    GPIO.output(TRIG,False)
    print ("Waiting For Sensor To Settle ")
    time.sleep(0.1)

    # ON for 1 micro sec
    GPIO.output(TRIG,True)
    time.sleep(0.00001)

    # OFF again
    GPIO.output(TRIG,False)


    # measuring distance depending on time
    while GPIO.input(ECHO)==0:
        pulse_start = time.time()

    while GPIO.input(ECHO)==1:
        pulse_end = time.time()

    # equation for measuring distance
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration *17150
    distance = round (distance , 2)


    return distance

def IR():
    GPIO.setup(3,GPIO.IN)
    GPIO.setup(5,GPIO.OUT)

    while True :
        val = GPIO.input(3)
        print(val)
        if val == 1:
            GPIO.output(5,GPIO.LOW)
        else :
            GPIO.output(5,GPIO.HIGH)

def humidity_HMC5883L():
    i2c_HMC5883l = HMC5883(gauss=1.3)
    i2c_HMC5883l.set_declination(0, 0)

    while True:
        print(i2c_HMC5883l.get_heading())
        sleep(1)

def camera():
    camera.start_preview()
    sleep(3)
    camera.capture('/home/pi/Desktop/image.jpg')
    camera.stop_preview()

def servo():
    p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
    p.start(0) # Initialization
    try:
      while True:
          p.ChangeDutyCycle(7.5)
          time.sleep(4)
          # call camera function
          p.ChangeDutyCycle(8)
          time.sleep(0.1)
          p.ChangeDutyCycle(8.5)
          time.sleep(0.1)
          p.ChangeDutyCycle(9)
          time.sleep(0.1)
          p.ChangeDutyCycle(9.5)
          time.sleep(0.1)
          p.ChangeDutyCycle(10)
          time.sleep(0.1)
          p.ChangeDutyCycle(10.5)
          time.sleep(0.1)
          p.ChangeDutyCycle(11)
          time.sleep(0.1)
          p.ChangeDutyCycle(11.5)
          time.sleep(0.1)
          p.ChangeDutyCycle(12)
          time.sleep(0.1)
          p.ChangeDutyCycle(12.5)
          time.sleep(4)

          camera()

          p.ChangeDutyCycle(12)
          time.sleep(0.1)
          p.ChangeDutyCycle(11.5)
          time.sleep(0.1)
          p.ChangeDutyCycle(11)
          time.sleep(0.1)
          p.ChangeDutyCycle(10.5)
          time.sleep(0.1)
          p.ChangeDutyCycle(10)
          time.sleep(0.1)
          p.ChangeDutyCycle(9.5)
          time.sleep(0.1)
          p.ChangeDutyCycle(9)
          time.sleep(0.1)
          p.ChangeDutyCycle(8.5)
          time.sleep(0.1)
          p.ChangeDutyCycle(8)
          time.sleep(0.1)
          p.ChangeDutyCycle(7.5)
          time.sleep(0.1)
          p.ChangeDutyCycle(7)
          time.sleep(0.1)
          p.ChangeDutyCycle(6)
          time.sleep(0.1)
          p.ChangeDutyCycle(5.5)
          time.sleep(0.1)
          p.ChangeDutyCycle(5)
          time.sleep(0.1)
          p.ChangeDutyCycle(4.5)
          time.sleep(0.1)
          p.ChangeDutyCycle(4)
          time.sleep(0.1)
          p.ChangeDutyCycle(3.5)
          time.sleep(0.1)
          p.ChangeDutyCycle(3)
          time.sleep(0.1)
          p.ChangeDutyCycle(2.5)
          time.sleep(0.1)
          p.ChangeDutyCycle(2)
          time.sleep(0.1)
          p.ChangeDutyCycle(1.5)
          time.sleep(0.1)
          p.ChangeDutyCycle(1)
          time.sleep(0.1)
          p.ChangeDutyCycle(0.5)
          time.sleep(0.1)
          p.ChangeDutyCycle(0)
          time.sleep(4)

          camera()

          p.ChangeDutyCycle(0.5)
          time.sleep(0.1)
          p.ChangeDutyCycle(1)
          time.sleep(0.1)
          p.ChangeDutyCycle(1.5)
          time.sleep(0.1)
          p.ChangeDutyCycle(2)
          time.sleep(0.1)
          p.ChangeDutyCycle(1.5)
          time.sleep(0.1)
          p.ChangeDutyCycle(3)
          time.sleep(0.1)
          p.ChangeDutyCycle(3.5)
          time.sleep(0.1)
          p.ChangeDutyCycle(4)
          time.sleep(0.1)
          p.ChangeDutyCycle(4.5)
          time.sleep(0.1)
          p.ChangeDutyCycle(5)
          time.sleep(0.1)
          p.ChangeDutyCycle(5.5)
          time.sleep(0.1)
          p.ChangeDutyCycle(6)
          time.sleep(0.1)
          p.ChangeDutyCycle(6.5)
          time.sleep(0.1)
          p.ChangeDutyCycle(7)
          time.sleep(0.1)
          
          camera()



    except KeyboardInterrupt:
      p.stop()
      GPIO.cleanup()


#===================================================================================================
# ========================
# -- Rover driving code --
# ========================
'''
while True: ultrasonic() --> ultrasonic sensor works all times
if distance <= 0.2:

- rover goes forward for 2 meters(specific number of wheel turns) (calculated by the diameter of the wheel)
- stop and call camera servo function
- servo make its function and call camera to take images

previos steps will be repeated 4 times
if i = 4 : the rover must be at the initial position and has finished the loop
'''

# enable ultra sonic sensor
def enable_ultrasonic():
    while True:
        ultra_sonic()
    
    # Obstacle avoidance
    if distance <= 20:
        right()
        time.sleep(2)

        left()
        time.sleep(2)

        left()
        time.sleep(2)

        right()
        time.sleep(2)




# mapping
def mapping():
    forward()
    time.sleep(4)

    right()
    time.sleep(4)

    right()
    time.sleep(4)

    right()
    time.sleep(4)