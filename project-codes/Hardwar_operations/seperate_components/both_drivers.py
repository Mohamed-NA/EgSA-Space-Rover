import time
import RPi.GPIO as GPIO

# PINs Definition
# 3 Drivers 

# Frist Driver - Right
Driver_1_Right_IN1 = 5
Driver_1_Right_IN2 = 6
Driver_1_Right_IN3 = 7
Driver_1_Right_IN4 = 8
Driver_1_Right_ENA = 12 #PWM
Driver_1_Right_ENB = 12 #PWM

# 2nd Driver - Left
Driver_2_Left_IN1 = 9
Driver_2_Left_IN2 = 10
Driver_2_Left_IN3 = 11
Driver_2_Left_IN4 = 14
Driver_2_Left_ENA = 13 #PWM
Driver_2_Left_ENB = 13 #PWM

# 3rd Driver
Driver_3_LastRL_IN1 = 15 # Right one back
Driver_3_LastRL_IN2 = 16 # Right one back   
Driver_3_LastRL_IN3 = 17 # Left one back
Driver_3_LastRL_IN4 = 20 # Left one back
Driver_3_LastRL_ENA = 18 # PWM
Driver_3_LastRL_ENB = 18 # PWM



# PINS Setup

GPIO.setmode(GPIO.BCM)

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



# Movement Functions

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




while(1):
    forward()
    time.sleep(2)
    back()
    time.sleep(2)

GPIO.cleanup()



























