def fibonacci(n):
    a,b=0,1
    for i in range(n):
        
        print(a,end=' ')
        a,b=b,a+b
    
fibonacci(5)

print()


def table(n):
    for i in range(1,n):
        print(f"{n} *{i} = {n*i}")
table(11)



def largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= c:
        return b
    else:
        return c

print(largest(10, 20, 15))

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

print(factorial(5))

def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

print(is_prime(13))
print(is_prime(15))

def list_sum(nums):
    total = 0
    for i in nums:
        total += i
    return total

numbers = [10, 20, 30, 40]
print(list_sum(numbers))