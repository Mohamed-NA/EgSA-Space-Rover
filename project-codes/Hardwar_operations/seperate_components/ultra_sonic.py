import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# setting ultra sonic pins
TRIG = 23
ECHO = 24
# m11 =12
# m12=16


# print("Distance Measurement in Progress")

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(m11, GPIO.OUT)
GPIO.setup(m12, GPIO.OUT)
time. sleep (5)
count=0


try:
    while True:

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

        # Check whether the distance is within 20 cm range
#         if distance <= 20:
#             count = count+1
#
#             # stopping motors
#             GPIO.output(m11, 0)
#             GPIO.output(m12, 0)
#
#             time.sleep(1)
#             GPIO.output(m11, 1)
#             GPIO.output(m12, 0)
#             time.sleep(1.5)
#         elif(count%2 ==1) and (flag==0):
#             GPIO.output(m11, 1)
#             GPIO.output(m12, 0)
#             flag=0
#         print ("Distance:", distance , "cm")
#
# except KeyboardInterrupt:
#     print("Cleaning up!")
#     GPIO.cleanup()
