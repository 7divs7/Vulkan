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
    SetAngle(90)


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

def edge_case_left_odd():
    left()
    stop()
    edge_backward()
    stop()
    left()
    stop()
    edge_forward()
    stop()

def edge_case_right_even():
    right()
    stop()
    edge_backward()
    stop()
    right()
    stop()
    edge_forward()
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
    print(arr)
    # arr = [[True, True, True, True, True, True, True, True, True, True], [True, True, True, False, False, True, True, True, True, True]]
    
    for r in range(len(arr)):
        for i in arr[r]:
            if i==True:
                pen_down()
            pen_up()
            stop()
            forward()
            stop()
        if r % 2 == 0:
            edge_case_right_even()
        else:
            edge_case_left_odd()
            
main()
GPIO.cleanup
