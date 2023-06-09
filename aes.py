def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array. """
    byte_array = bytearray()  # 빈 bytearray 객체를 생성합니다.

    for row in matrix:  # 행렬의 각 행을 순회합니다.
        for num in row:  # 행의 각 요소를 순회합니다.
            byte_array.append(num)  # 요소의 정수 값을 bytearray에 추가합니다.

    return bytes(byte_array)  # bytearray를 bytes 객체로 변환하여 반환합니다.


matrix = [
    [99, 114, 121, 112],
    [116, 111, 123, 105],
    [110, 109, 97, 116],
    [114, 105, 120, 125],
]

print(matrix2bytes(matrix))
