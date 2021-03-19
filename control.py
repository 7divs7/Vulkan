import RPi.GPIO as GPIO
from time import sleep as Sleep

GPIO.setwarnings(False)

# Wheel Control
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(31,GPIO.OUT)

def forward():
    GPIO.output(37,GPIO.LOW)
    GPIO.output(35,GPIO.HIGH)
    GPIO.output(33,GPIO.HIGH)
    GPIO.output(31,GPIO.LOW)
    Sleep(0.2)

def edge_forward():
    GPIO.output(37,GPIO.LOW)
    GPIO.output(35,GPIO.HIGH)
    GPIO.output(33,GPIO.HIGH)
    GPIO.output(31,GPIO.LOW)
    Sleep(0.535)

def edge_backward():
    GPIO.output(37,GPIO.HIGH)
    GPIO.output(35,GPIO.LOW)
    GPIO.output(33,GPIO.LOW)
    GPIO.output(31,GPIO.HIGH)
    Sleep(0.265)

def left():
    GPIO.output(37,GPIO.LOW)
    GPIO.output(35,GPIO.LOW)
    GPIO.output(33,GPIO.HIGH)
    GPIO.output(31,GPIO.LOW)
    Sleep(0.43)

def right():
    GPIO.output(37,GPIO.LOW)
    GPIO.output(35,GPIO.HIGH)
    GPIO.output(33,GPIO.LOW)
    GPIO.output(31,GPIO.LOW)
    Sleep(0.43)
    
def stop():
    GPIO.output(37,GPIO.LOW)
    GPIO.output(35,GPIO.LOW)
    GPIO.output(33,GPIO.LOW)
    GPIO.output(31,GPIO.LOW)
    Sleep(3)

for i in range(10):
    forward()
    stop()

right()
stop()

edge_backward()
stop()

right()
stop()

edge_forward()
stop()

GPIO.cleanup
