import math
import string

p = 19
q = 31
n = p * q
phi = (p - 1) * (q - 1)

for e in range(2, phi):
    if all(e % i != 0 for i in range(2, int(e**0.5) + 1)):
        if math.gcd(e, phi) == 1:
            break

P = "TRANTHINGAN"

numbers = [ord(ch) - ord('A') + 1 for ch in P]

C = [pow(m, e, n) for m in numbers]

print("n =", n)
print("phi(n) =", phi)
print("e =", e)
print("Thong diep:", P)
print("Dãy số ban đầu:", numbers)
print("Bản mã RSA:", C)