# code for terminal in raspberry pi
# sudo apt_get install python3-rpi.GPIO
# pip3 install gpiozero


# this code to make servo go to initial position, wait 4 sec go left then go right
# ================================================================================


import RPi.GPIO as GPIO
import time

servoPIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

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
      # call camera function
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
      # call camera function
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
      # back to initial position again



except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()
