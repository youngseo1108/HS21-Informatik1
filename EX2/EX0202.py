'''
Transform the following mathematical expression into a Python program 
to be able to calculate the result for arbitrary values of a, b, c, and d 
defined in the source code:

a - (b^2 / (c - d * (a + b)))

Implement it in a function calculate where it should be returned.
'''
a = 1
b = 2
c = 3
d = 4

# Change the function below to calculate the result
# with the given formula:
# `a - (b^2 / (c - d * (a + b)))`
# You must use the variables defined above.
def calculate():
    res = a - (b**2 / (c - d * (a + b)))
    # You don't need to change the following line.
    # It simply returns the value calculated above.
    return res

calculate()