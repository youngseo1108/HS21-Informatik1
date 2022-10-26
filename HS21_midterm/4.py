'''
Implement a function no_unlucky, which takes two parameters: a list of integers values, and an integer unlucky.

The function should sum up all those values in values which are not divisible by unlucky. 
If unlucky is 0 all values in values should be summed up. 
Return the resulting sum from the function.

You can assume that the function is only called with valid parameters.
'''
def no_unlucky(values, unlucky):
    total = 0
    for value in values:
        if unlucky == 0:
            total += value
        else:
            if value % unlucky != 0:
                total += value
    # sum up all those values in values which are not divisible by unlucky
    # If unlucky is 0 all values in values should be summed up.
    return total

assert(no_unlucky([10, 24, 1], 13) == 35)
assert(no_unlucky([13, 25], 13) == 25)
assert(no_unlucky([13, 26], 13) == 0)