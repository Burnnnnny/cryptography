def encrypt_caesar(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            if char.islower():
                base = ord('a')
            else:
                base = ord('A')
            encrypted_char = chr((ord(char) - base + shift) % 26 + base)
            ciphertext += encrypted_char
        else:
            ciphertext += char
    return ciphertext

def decrypt_caesar(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            if char.islower():
                base = ord('a')
            else:
                base = ord('A')
            decrypted_char = chr((ord(char) - base - shift) % 26 + base)
            plaintext += decrypted_char
        else:
            plaintext += char
    return plaintext

# 사용자 입력 받기
plaintext = input("평문을 입력하세요: ")
shift = int(input("키 값을 입력하세요: "))

# 암호화
ciphertext = encrypt_caesar(plaintext, shift)
print("암호화된 문장:", ciphertext)

# 복호화
decrypted_text = decrypt_caesar(ciphertext, shift)
print("복호화된 문장:", decrypted_text)
