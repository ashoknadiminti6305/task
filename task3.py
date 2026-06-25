# Armstrong Number Check

num =153

temp = num
length = len(str(num))      # Find length of number
total = 0

while temp > 0:
    digit = temp % 10       # Separate each digit
    total += digit ** length  # digit power length
    temp //= 10

print("Sum =", total)

if total == num:           # Check condition
    print(num, "is an Armstrong Number")
else:
    print(num, "is not an Armstrong Number")