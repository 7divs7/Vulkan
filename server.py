import socket
import time
import pickle
import cv2

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 6666))
s.listen(5)

while True:

    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")

    d = cv2.imread("pic_input.png",3)
    
    msg = pickle.dumps(d)
    msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8')+msg
    clientsocket.send(msg)