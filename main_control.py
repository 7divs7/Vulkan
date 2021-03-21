import RPi.GPIO as GPIO
from time import sleep as Sleep
import socket 
import pickle

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

def edge_case():
    backward()
    stop()

def main():
    HOST = '192.168.1.6'
    PORT = 6969
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    print('Connected by', addr)
    arr = []
    while 1:
        data = conn.recv(4096)
        if not data: break
        # conn.send(data)
        arr = pickle.loads(data)
    conn.close()
    
    for i in range(len(arr)):
        if i%2!=0:
            arr[i].reverse()
    print(arr)

    
    pwm.start(20)
    for r in range(len(arr)):
        if r%2 == 0:
            for i in arr[r]:
                if i==True:
                    pen_down()
                pen_up()
                stop()
                right()
                stop()
        else:
            for i in arr[r]:
                if i==True:
                    pen_down()
                pen_up()
                stop()
                left()
                stop()
        edge_case()
    
    pwm.stop()
    
main()
GPIO.cleanup
