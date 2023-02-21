from pwn import *
import re
import pyfiglet  
import time
result = pyfiglet.figlet_format("A J I T", font = "alphabet" )
print(result)
#l = listen(2001)
r = remote('43.204.232.3', 2002) 
#svr = l.wait_for_connection()
print(r.recv())
name='ajit'
r.send(b'name')
print(r.recv().decode())

res=r.recv().decode()
print(res)
x=(input())
y=(input())
#c=(input())
#d=(input())
#e=(input())
#f=(input())
def add(a, b):
    number = int(a) + int(b)
    return number

sumNum=add(x,y)
print(sumNum)
bytes_val = sumNum.to_bytes(3, 'big')
  
# printing integer in byte representation
print(bytes_val)
r.send_raw(bytes_val)
print(r.recv().decode())
print(r.recv().decode())
ASCII_CHARS = ["-", "|", "/", "'", "*", "+", ";", ":", ",", "."]
