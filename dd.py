hex_values = ['0x7b', '0x53', '0x7b', '0x53', '0x69', '0x6e', '0x5f', '0x69', '0x70', '0x5f', '0x53', '0x61', '0x6e', '0x67', '0x5f', '0x42', '0x61', '0x6e', '0x67', '0x5f', '0x47', '0x61', '0x5f', '0x42', '0x61', '0x6e', '0x67', '0x5f', '0x47', '0x61']

byte_array = bytearray(int(hex_value, 16) for hex_value in hex_values)

print(byte_array)
