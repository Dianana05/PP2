#1
import math
n=int(input("n="))
radian=math.radians(n)
print(radian)

#2
import math
a=int(input("first v="))
b=int(input("second v="))
h=int(input("height="))
s=((a+b)/2)*h
print("aree of trapezoid=", s)

#3
import math
n=int(input("number of sides="))
a=int(input("side length="))
pi=3.14
s=(n*a**2)/4*math.tan(math.pi/n)
print("are of polygon:", round(s))

#4
import math
a=int(input("length="))
b=int(input("height="))
s=float(a*b)
print("area of parallelogram=", s)