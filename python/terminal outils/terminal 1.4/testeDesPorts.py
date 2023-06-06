import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex(('127.0.0.1',80))
if result == 0:
   print("Port is open")
else:
   print("Port is not open")
sock.close()

# coding: utf-8



hote = "localhost"
port = 15555

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect_ex(('127.0.0.1', 80))
print ("Connection on {}".format(80))

socket.send("Hey my name is Olivier!")

print ("Close")
socket.close()