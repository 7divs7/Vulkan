import RPi.GPIO as GPIO
from time import sleep as Sleep

GPIO.setwarnings(False)

# Wheel Control
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(31,GPIO.OUT)

GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

pwm = GPIO.PWM(16,100)


def forward():
    GPIO.output(37,GPIO.LOW)           #back right
    GPIO.output(35,GPIO.HIGH)
    GPIO.output(33,GPIO.HIGH)          #back left
    GPIO.output(31,GPIO.LOW)
    
    GPIO.output(11,GPIO.LOW)           #front right
    GPIO.output(13,GPIO.HIGH)
    GPIO.output(15,GPIO.LOW)           #front left
    GPIO.output(18,GPIO.HIGH)
    
    Sleep(3)


def backward():
    GPIO.output(37,GPIO.HIGH)           #back right
    GPIO.output(35,GPIO.LOW)
    GPIO.output(33,GPIO.LOW)            #back left
    GPIO.output(31,GPIO.HIGH)
    
    GPIO.output(11,GPIO.HIGH)           #front right
    GPIO.output(13,GPIO.LOW)
    GPIO.output(15,GPIO.HIGH)           #front left
    GPIO.output(18,GPIO.LOW)
    
    Sleep(3)


def right():
    GPIO.output(37,GPIO.LOW)           #back right
    GPIO.output(35,GPIO.HIGH)
    GPIO.output(33,GPIO.LOW)          #back left
    GPIO.output(31,GPIO.HIGH)

    GPIO.output(11,GPIO.HIGH)           #front right
    GPIO.output(13,GPIO.LOW)
    GPIO.output(15,GPIO.LOW)           #front left
    GPIO.output(18,GPIO.HIGH)

    Sleep(3)


def left():
    GPIO.output(37,GPIO.HIGH)           #back right
    GPIO.output(35,GPIO.LOW)
    GPIO.output(33,GPIO.HIGH)          #back left
    GPIO.output(31,GPIO.LOW)

    GPIO.output(11,GPIO.LOW)           #front right
    GPIO.output(13,GPIO.HIGH)
    GPIO.output(15,GPIO.HIGH)           #front left
    GPIO.output(18,GPIO.LOW)

    Sleep(3)
    
def stop():
    GPIO.output(37,GPIO.LOW)
    GPIO.output(35,GPIO.LOW)
    GPIO.output(33,GPIO.LOW)
    GPIO.output(31,GPIO.LOW)

    GPIO.output(11,GPIO.LOW)
    GPIO.output(13,GPIO.LOW)
    GPIO.output(15,GPIO.LOW)
    GPIO.output(18,GPIO.LOW)

    Sleep(3)

def main():
    pwm.start(20)
    left()
    stop()
    pwm.stop()
    #left()
    #stop()
    #right()
    #stop()
main()
GPIO.cleanup
