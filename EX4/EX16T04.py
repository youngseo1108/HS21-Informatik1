'''
In this exercise you will write two separate functions: 
one should be invoked by the other, while at the same time leveraging recursion.

Specification

The goal is to write a function gcd(a,b) that returns the greatest common divisor of a and b:
- The gcd(a,b) function should call itself recursively
- The gcd(a,b) function should be able to handle mistakenly entered negative numbers by converting them to positives
- To achieve this, the gcd(a,b) should leverage the absolute_value(a) function
- If a and b is zero, None should be returned
- If either a or b is zero, but not both, the absolute value of the parameter which is not zero should be returned
- gcd(a,b) should work in both cases a < b and a > b

Hints
Break it down into chunks; start with only the recursive task and case a > b
Start from the base case of the recursion
Think of the step closest before the base case; What is the difference?
Writing tests will help you!
Note: Starting with this exercise, we will provide public tests that fail by default. The tests we provide will pass for a correct solution, but keep in mind that the grading system runs many more exhaustive tests, so if the public test passes, that does not necessarily mean that your solution is 100% correct, as it might fail on certain edge or corner cases.

Note: The provided script defines the signature of the functions. Do not change this signature or the automated grading will fail.
'''
import os

def absolute_value(a):
    if a < 0:
        return -a
    return a

def gcd(a, b):
    # If a and b is zero, None should be returned
    if a == b == 0:
        return None
    elif absolute_value(b) == 0:
        return absolute_value(a)
    return gcd(absolute_value(b), absolute_value(a) % absolute_value(b))

a = 33
b = 17
print(f"greatest common divisor of {a} and {b} is = {gcd(a, b)}")