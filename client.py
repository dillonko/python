import socket
import time

i = 0
print("Starting up...")
host = raw_input("Host>")
print("Connecting to host...")
time.sleep(1)
print("Please wait...")
port = input("Port>")
time.sleep(1)
t = input("Time>")
print("Connected.")
print("Recieving data.")

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))

while (i < t):
	print ("Recieved: " + s.recv(1024))
	time.sleep(1)
	i = i + 1