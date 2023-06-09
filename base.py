import base64

i = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
i_bytes = bytes.fromhex(i)

b = base64.b64encode(i_bytes)

print(b)
