import socket
import sys
import os
import subprocess
hn = socket.gethostname()
hip = socket.gethostbyname(hn)
print("SCOS Core Terminal")
while True:
    com = input(">>>")
    if com == "lts":
     print("abcdefghijklmnopqrstuvwxyz")
     print("1234567890")
    if com == "linux":
        subprocess.run("sh")
    if com == "win":
        subprocess.run("cmd")
