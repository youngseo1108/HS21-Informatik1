'''
Implement a function compute that takes 3 numbers (integers and/or floats) as parameters 
and returns the result of the mathematical formula shown below, 
rounded to the nearest integer using round(). (The vertical bars indicate an absolute value.)

(x+2y)+|z|5
    return round(((x+2**y)+abs(z))**(1/5))
'''
# compute(10,20,30) should return 16
def compute(x, y, z):
    return round(((x+2**y)+abs(z))**(1/5))

print(compute(10,20,30))