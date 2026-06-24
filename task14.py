# Bitwise Operators Practice

a = 5
b = 5

# XOR of same values
print("XOR (5 ^ 5) =", a ^ b)   # 0

# AND operation
print("AND (5 & 5) =", a & b)   # 5

# Check 1 is even or odd
n = 1
if n & 1:
    print(n, "is Odd")
else:
    print(n, "is Even")

# All Bitwise Operators
x = 5  # 0101
y = 3  # 0011

print("AND (&)         :", x & y)   # 1
print("OR (|)          :", x | y)   # 7
print("XOR (^)         :", x ^ y)   # 6
print("NOT (~x)        :", ~x)      # -6
print("Left Shift (<<) :", x << 1)  # 10
print("Right Shift(>>) :", x >> 1)  # 2