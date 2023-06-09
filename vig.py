def vigenere_decrypt(ciphertext, key):
    decrypted_text = ""
    key_length = len(key)
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            # 알파벳 문자에 대해서만 해독을 시도합니다.
            key_char = key[key_index].upper()
            key_index = (key_index + 1) % key_length

            if char.isupper():
                # 대문자인 경우
                decrypted_char = chr((ord(char) - ord(key_char) + 26) % 26 + ord('A'))
            else:
                # 소문자인 경우
                decrypted_char = chr((ord(char) - ord(key_char) + 26) % 26 + ord('a'))

            decrypted_text += decrypted_char
        else:
            # 알파벳이 아닌 경우 그대로 추가합니다.
            decrypted_text += char

    return decrypted_text


# 사용자 입력을 받아 해독을 수행합니다.
ciphertext = input("암호화된 텍스트를 입력하세요: ")
key = input("키 값을 입력하세요: ")

decrypted_message = vigenere_decrypt(ciphertext, key)
print("해독된 텍스트:", decrypted_message)
