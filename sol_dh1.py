def modinv(g, p):
  """
  Finds the modular inverse of g modulo p.

  Args:
    g: The number to find the inverse of.
    p: The modulus.

  Returns:
    The modular inverse of g modulo p.
  """

  # Use the extended Euclidean algorithm to find the modular inverse.
  """
  확장 유클리드 알고리즘을 사용하여 g의 p에 대한 모듈러 역수를 찾습니다.
  """
  g, x, y = extended_euclidean_algorithm(g, p)

  # The modular inverse is the x-coordinate of the extended Euclidean
  # algorithm, modulo p.
  """
  모듈러 역수는 확장 유클리드 알고리즘의 x-좌표입니다.
  """
  return x % p


def extended_euclidean_algorithm(a, b):
  """
  Finds the greatest common divisor of a and b, and the x and y coordinates
  of the Bezout equation a * x + b * y = gcd(a, b).

  Args:
    a: The first number.
    b: The second number.

  Returns:
    A tuple of (gcd(a, b), x, y).
  """

  # Base case.
  """
  기본 사례입니다.
  """
  if b == 0:
    return (a, 1, 0)

  # Recursive case.
  """
  재귀 사례입니다.
  """
  gcd, x1, y1 = extended_euclidean_algorithm(b, a % b)
  x = y1
  y = x1 - (a // b) * y1

  return (gcd, x, y)


p = 991
g = 209

# Find the modular inverse of g modulo p.
"""
g의 p에 대한 모듈러 역수를 찾습니다.
"""
d = modinv(g, p)

print(d)
