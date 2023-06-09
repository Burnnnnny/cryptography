from pwn import *

a = 'label'
b = 13

c = xor(a,b)
print(c)