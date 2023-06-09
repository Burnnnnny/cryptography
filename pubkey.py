from Crypto.PublicKey import RSA
import base64

# 공개 키 파일(.txt)의 경로
file_path = 'public_key.txt'

# .txt 파일에서 공개 키 문자열 읽기
with open(file_path, 'r') as f:
    key_data = f.read()

# .txt 파일에서 PEM 형식의 공개 키 추출
key_start = '-----BEGIN PUBLIC KEY-----'
key_end = '-----END PUBLIC KEY-----'
key_data = key_data[key_data.find(key_start) + len(key_start):key_data.find(key_end)].strip()

# PEM 형식의 공개 키 디코딩
decoded_key = base64.b64decode(key_data)

# RSA 공개 키 객체 생성
public_key = RSA.import_key(decoded_key)

# e와 N 값 추출
e = public_key.e
N = public_key.n

# 추출된 e와 N 값 출력
print('e:', e)
print('N:', N)

