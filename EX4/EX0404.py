'''
TASK 4. Greatest Common Divisor Recursion
1. gcd(a,b)
- returns the greatest common divisor of a and b:
- call itself recursively
- able to handle mistakenly entered negative numbers by converting them to positives

-> To achieve this, leverage the absolute_value(a) function
- a and b is zero, None should be returned
- either a or b is zero (not both) -> return the abs value of the non-zero param
- gcd(a,b) should work in both cases a < b and a > b

Hints
Break it down into chunks; start with only the recursive task and case a > b
Start from the base case of the recursion
Think of the step closest before the base case; What is the difference?
Writing tests will help you!
'''
import os

def absolute_value(a):
    if a < 0:
        return -a
    return a

#print(absolute_value(-1))
#print(absolute_value(10))
#print(absolute_value(0))

def gcd(a, b):
    # implement this function
    if a == b == 0:
        return None
    elif absolute_value(b) == 0:
        return absolute_value(a)
    else:
        return gcd(absolute_value(b), absolute_value(a) % absolute_value(b))

# gcd(0, 0) should be None and not 0.

a = 33
b = 17
print(f"greatest common divisor of {a} and {b} is = {gcd(a, b)}")
print(gcd(-13, 39))
print(gcd(0,10))
print(gcd(11,0))
print(gcd(0,0))
print(gcd(0,-5))