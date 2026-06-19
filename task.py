import math
l=int(input("Enter length: "))
bd=int(input("Enter bredth: "))
h=int(input("Enter Height: "))
s=int(input("Enter side: "))
r=float(input("Enter Radius: "))
print("Area of Rectangle: ",l*bd)
print("Area of Square: ",s*s)
print("Area of Triangle: ",0.5*l*bd)
print("Area of Circle: ",math.pi*r**2)
print("Area of Parallelogram: ",bd*h)
d1=int(input("enter d1: "))
d2=int(input("Enter d2: "))
print("Area of Rhombus: ",0.5*d1*d2)
a=int(input("enter value of a:"))
b=int(input("enter value of b:"))
print("Area of Trapezium: ",(0.5)*(a+b)*h)
print("Area of Equilateral Triangle: ",(math.sqrt(3)/4)*a*a)
theta = float(input("Enter angle (in degrees): "))
area = (theta / 360) * math.pi * r * r
print("Area of sector of a circle =", area)
print("Area of semicircle =", (0.5)*math.pi*r**2)

#perimeter
print("Perimeter of Rectangle: ",2*(l+b))
print("perimeter of Square: ",4*s)
c=int(input("Enter a value c:"))
print("perimeter of Triangle: ",a+b+c)
print("perimeter of Circle: ",2*math.pi*r)
print("perimeter of Parallelogram: ",2*(a+b))
print("perimeter of Rhombus: ",4*a)
print("perimeter of regular pentagon: ",5*a)
print("perimeter of regular hexagon: ",6*a)
print("perimeter of Equilateral Triangle: ",3*a)

#cube
print("Volume of a cube: ",a**3)
print("Total Surface Area of a Cube: ",6*a**2)
n=int(input("Enter a value n:"))
print("Lateral Surface Area of a Cube: ",4*a**2)
print("Cube of a Number: ",n**3)
print("Sum of Cubes of Two Numbers: ",(a**3)+(b**3))
print("Difference of Cubes of Two Numbers: ",(a**3)-(b**3))
N = int(input("Enter N: "))

for i in range(1, N + 1):
    print(f"{i}³ = {i**3}")

num= float(input("Enter a number: "))

cube_root = num ** (1/3)

print("Cube Root =", cube_root)

num1 = int(input("Enter N: "))

root = int(num1 ** (1/3))
largest_cube = root ** 3

print("Largest cube <=", num1, "is", largest_cube)