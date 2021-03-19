import socket
import pickle

HOST = '192.168.1.6'
PORT = 6969
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print('Connected by', addr)
while 1:
    data = conn.recv(4096)
    if not data: break
    # conn.send(data)
    print(pickle.loads(data))
conn.close()