'''
TASK 1. Is this number a prime?

prime number: a number > 1 that can only be divided by itself & 1 
Write a function is_prime that takes a positive integer as an argument 
and checks whether it is prime or not.

Depending on the result, the function should return 
- the strings x is prime (for prime numbers) 
- x is not a prime number (a * b = x) with the smallest possible a 
(for non-prime numbers), showing the actual values for x, a and b. 

e.g. is_prime(12)
return the string 12 is not a prime number (2 * 6 = 12). 

By definition, 1 is not a prime number, the function should return 
the string 1 is the multiplicative identity. 

You can assume that only values greater than 0 will be passed to this 
function.
'''
def is_prime(n):
    # implement this function
    # n  == 1
    if n == 1:
        return '1 is the multiplicative identity'
    for i in range(2, n//2):
        if (n % i) == 0:
            return f'{n} is not a prime number ({i} * {int(n/i)} = {n})'
            break
    return f'{n} is prime'

print(is_prime(15))
print(is_prime(1))
print(is_prime(17))
print(is_prime(100))