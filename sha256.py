import hashlib

def sha256_hash(data):
    # 데이터를 SHA-256 해시값으로 변환하는 함수
    sha256 = hashlib.sha256()
    sha256.update(data)
    return sha256.hexdigest()

# 해시할 데이터
data = b"crypto{Immut4ble_m3ssag1ng}"

# 데이터의 SHA-256 해시값 계산
hash_value = sha256_hash(data)

# 결과 출력
print("SHA-256 해시값:", hash_value)
