import math

# Variables
a = 20
b = 5
x = 10
y = 3

# ---------------- Arithmetic Expressions ----------------
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Power:", a ** b)

# ---------------- Relational Expressions ----------------
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

# ---------------- Logical Expressions ----------------
print("AND:", a > 10 and b < 10)
print("OR:", a < 10 or b < 10)
print("NOT:", not(a > b))

# ---------------- Assignment Expressions ----------------
c = a
c += b
print("+= :", c)
c -= 2
print("-= :", c)
c *= 2
print("*= :", c)
c /= 2
print("/= :", c)

# ---------------- Bitwise Expressions ----------------
print("AND (&):", a & b)
print("OR (|):", a | b)
print("XOR (^):", a ^ b)
print("NOT (~):", ~a)
print("Left Shift:", a << 2)
print("Right Shift:", a >> 2)

# ---------------- Membership Expressions ----------------
lst = [10, 20, 30, 40]
print("20 in list:", 20 in lst)
print("50 not in list:", 50 not in lst)

# ---------------- Identity Expressions ----------------
l1 = [1, 2]
l2 = l1
l3 = [1, 2]
print("l1 is l2:", l1 is l2)
print("l1 is l3:", l1 is l3)

# ---------------- Conditional Expression ----------------
print("Greater Number:", a if a > b else b)



# ---------------- Mathematical Formulas ----------------
length = 10
breadth = 5
side = 4
radius = 7
pi = math.pi

print("Area of Rectangle:", length * breadth)
print("Perimeter of Rectangle:", 2 * (length + breadth))
print("Area of Square:", side ** 2)
print("Perimeter of Square:", 4 * side)
print("Area of Circle:", pi * radius ** 2)
print("Circumference:", 2 * pi * radius)
print("Volume of Cube:", side ** 3)
print("Square Root:", math.sqrt(64))
print("Cube Root:", 27 ** (1 / 3))
print("Absolute Value:", abs(-25))
print("Maximum:", max(a, b))
print("Minimum:", min(a, b))

# ---------------- Interest ----------------
P = 10000
R = 5
T = 2

SI = (P * R * T) / 100
CI = P * (1 + R / 100) ** T - P

print("Simple Interest:", SI)
print("Compound Interest:", CI)

# ---------------- Average & Percentage ----------------
m1, m2, m3 = 80, 90, 85
avg = (m1 + m2 + m3) / 3
percentage = ((m1 + m2 + m3) / 300) * 100

print("Average:", avg)
print("Percentage:", percentage)

# ---------------- Temperature Conversion ----------------
celsius = 37
fahrenheit = (celsius * 9 / 5) + 32
print("Celsius to Fahrenheit:", fahrenheit)

fahrenheit = 98.6
celsius = (fahrenheit - 32) * 5 / 9
print("Fahrenheit to Celsius:", celsius)

# ---------------- Distance Formula ----------------
x1, y1 = 2, 3
x2, y2 = 6, 7
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print("Distance:", distance)



# ---------------- Swap ----------------
n1 = 10
n2 = 20
n1, n2 = n2, n1
print("Swapped:", n1, n2)

# ---------------- List, Set & Dictionary Comprehension ----------------
print("List:", [i * i for i in range(1, 6)])
print("Set:", {i * i for i in range(1, 6)})
print("Dictionary:", {i: i * i for i in range(1, 6)})

