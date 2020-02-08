# Program to find root of equation

import cmath
a=int(input("enter the value of a"))       #taking value of a from user
b=int(input("enter the value of b"))       #taking value of a from user
c=int(input("enter the value of c"))       #taking value of a from user
delta=((b*b)-(4*a*c))                      #find value of delta using formula
x=(-b+cmath.sqrt(delta))/(2*a)             #find 1st root of equation
y=(-b-cmath.sqrt(delta))/(2*a)             #find 2nd root of equation
print("the first root of equation",x)
print("the second root of equation",y)
