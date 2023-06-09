from pwn import *

ciphertext = ')":#?4kQXG\\1lVRl9$48'
key = xor(ciphertext, 'zdAWWQ4394mR3943akfE')
print(key)

	
#)":#?4kQXG\1lVRl9$48
#xor
#zdAWWQ4394mR3943akfE
