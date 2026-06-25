#square
n=int(input("enter a number: "))
print("\nSquare Pattern")
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()
#Right Triangle
print("\nRight Triangle")
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()
#Number Triangle
print("\nNumber Triangle")
for i in range(1,n):
    for j in range(1,i+1):
       print(j,end=" ")
    print()
#Repeated Number Triangle
print("\nRepeated Number Triangle")
for i in range(1,n):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
#Alphabet Triangle
print("\nAlphabet Triangle")
for i in range(n):
    for j in range(i+1):
        print(chr(65+j),end=" ")
    print()
#Inverted Star Triangle
print("\nInverted Star Triangle")
for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print()
#Inverted Number Triangle
print("\nInverted Number Triangle")
for i in range(n):
    for j in range(1,n-i):
        print(j,end=" ")
    print()
#Continuous Number Pattern
print("\nContinuous Number Pattern")
num=1
for i in range(n):
    for j in range(i+1):
        print(num,end=" ")
        num+=1
    print()
#Right-Aligned Star Triangle
print("\nRight-Aligned Star Triangle")
for i in range(1,n):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()
#Pyramid Pattern
print("\nPyramid Pattern")
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(2*i+1):
        print("*",end="")
    print()