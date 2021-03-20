import RPi.GPIO as GPIO
from time import sleep as Sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
# Servo Control
vertical = 5

GPIO.setup(vertical, GPIO.OUT)
pwm_v=GPIO.PWM(vertical, 50)
pwm_v.start(0)

def translate(value, leftMin, leftMax, rightMin, rightMax):
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin
    valueScaled = float(value - leftMin) / float(leftSpan)
    return rightMin + (valueScaled * rightSpan)

def SetAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(5, True)
    pwm_v.ChangeDutyCycle(duty)
    Sleep(1)
    GPIO.output(5, False)
    pwm_v.ChangeDutyCycle(0)

def pen_down():
    SetAngle(170)

def pen_up():
    SetAngle(0)


def main():
    pen_up()
    pen_down()

main()

GPIO.cleanup
