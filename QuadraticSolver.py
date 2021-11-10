"""
Create program to solve a quadratic equation and display its roots.
ask for values of a, b and c.
use the quadratic formula to solve and diplay both the roots.
"""
import time, math

def Quadratic(a, b, c):
    disc = math.sqrt((b**2) - (4*a*c))
    x1 = ((-b + disc)/(2*a))
    x2 = ((-b - disc)/(2*a))
    print("Roots of equation are : ")
    print("x\u2081 =",x1,"and x\u2082 =",x2)
    print("Thank you for running my program!")

print("Welcome to the quadratic equation solver!")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("A Quadratic equation is in the from of : ax\u00b2 + bx + c = 0")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
a = float(input("Enter a : "))
b = float(input("Enter b : "))
c = float(input("Enter c : "))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Thank you for entering the values.")
time.sleep(3)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
Quadratic(a, b, c)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
