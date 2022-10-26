'''
# TASK 3. Fuzz testing and white-box testing
1. 1st part: Fuzz testing
1.1 fuzzer
- takes four input parameters (all integers) 
- returns a string of random length containing random characters.
- min_length & max_length: determine how long the returned random string can be. 
- char_start & char_end: determine which character from the ASCII table should be included in the returned random string. 
e.g. fuzzer(5, 10, 43, 57) -> return a string that is between 5 and 10 (including) characters long 
and contains randomly selected characters corresponding to decimal numbers between 42 (+) and 57 (9) from the ASCII table. 
For this example, one such random string might be .5728//.

1.2 calculate_factorial
- takes one input parameter inp (an integer or a string) 
- returns the factorial of the input inp as an integer. 
- return None if the input is None. 
- If the input is a string, the function should try to convert the input string into an integer 
- and if this is not possible, the function should throw a TypeError with the message "TypeError: string". 
- If the converted number or integer input is negative -> throw a ValueError with the message "ValueError: number negative". 
- If the converted number or integer input is larger than 10 -> throw a ValueError but with the message "ValueError: number too large". 
This is for example a simulation of a buffer overflow.

1.3 run
- one input parameter trials (an integer)
- returns a list of tuples, containing feedback on executing the calculate_factorial function with random inputs. 
- The function run should run your function calculate_factorial as many times as specified in trials. 
- Each time calculate_factorial is run, it should be provided with a new random input obtained by calling the fuzzer function. 
- For the parameter input for the function fuzzer use the provided global variables instead of passing values directly to the function.
- For each run, a new tuple should be appended to the return value, where each tuple consists of two elements.
- The first element is an integer which can be 0 (success) or 1 (failure) and the second element contains a string.
- When calculate_factorial throws a ValueError, the error should be caught and a tuple with the elements 1 and the error message should be added to the list which will be returned. Any other thrown error should be caught and a tuple with the elements 1 and the string "Other error" should be added to the list. If no error is thrown, a tuple with the elements 0 and an empty string should be added to the list. If no element is added to the resulting list, an empty list should be returned.

Note: For the building a string of random range and with random characters these functions can help: randrange, chr
Note: Check out the lecture slides for raising and catching Errors/Exceptions.

2. 2nd part: White-box testing
White-box testing is about implementing tests by studying the implementation of a program. In this part of the task you should write text cases for the function calculate_factorial only.
You should test whether the function calculate_factorial throws the correct exceptions when supplied with invalid inputs and you should also test whether it works normally with valid input. To check whether a function throws an exception, have a look at self.assertRaises. You do not have to test the error messages themselves. As your function also should accept integers, test these cases as well. And remember to also test edge cases!
Note: With self.fail() you can make a test case fail.
'''
import random

min_length_global = 0
max_length_global = 5
char_start_global = 30
char_end_global = 65

# For this example, one such random string might be .5728//.
# randrange chr
def fuzzer(min_length, max_length, char_start, char_end):
    # min_length & max_length: determine how long the returned random string can be. 
    # char_start & char_end: determine which character from the ASCII table should be included in the returned random string. 
    n = random.randrange(min_length, max_length)
    res = ''
    while n > 0:
        res += chr(random.randrange(char_start,char_end))
        n -= 1
    # returns a string of random length containing random characters.
    return res

def calculate_factorial(inp):# inp (an integer or a string)
    # return None if the input is None. 
    if inp == None:
        return None
    
    if type(inp) == str:
    # If the input is a string, convert the input string into an integer
        try:
            inp = int(inp)
    # if not possible, throw a TypeError with the message "TypeError: string"
        except ValueError:
            raise TypeError('TypeError: string')

    # If the converted number or integer input is negative
    # -> throw a ValueError with the message "ValueError: number negative". 
    if inp < 0:
        raise ValueError('ValueError: number negative')
        
    # If the converted number or integer input is larger than 10
    # -> throw a ValueError but with the message "ValueError: number too large"
    if inp > 10:
        raise ValueError('ValueError: number too large')

    res = 1
    while inp > 0:
        res *= inp
        inp -= 1
    return res # returns the factorial of the input inp as an integer.

print(calculate_factorial(5))

def run(trials): # one input parameter trials (an integer)
    res = []
    while trials > 0:
        input = fuzzer(min_length_global, max_length_global, char_start_global, char_end_global)
        try:
            res.append((0,str(calculate_factorial(input))))
        except:
            res.append((1,'Other error'))
        trials -= 1
    return res

print(run(15))

#---------------------solution---------#
#!/usr/bin/env python3
from unittest import TestCase
from script3 import calculate_factorial

class MyTests(TestCase):

    def _assert(self, inp, expected):
        actual = calculate_factorial(inp)
        self.assertEqual(expected, actual)

    # tests calculate_factorial
    def test_None(self):
        self.assertEqual(None, calculate_factorial(None))

    def test_negative_numbers_integer(self):
        self.assertRaises(ValueError, calculate_factorial, -1)

    def test_negative_numbers_string(self):
        self.assertRaises(ValueError, calculate_factorial, "-1")

    def test_number_too_large_integer(self):
        self.assertRaises(ValueError, calculate_factorial, 11)

    def test_number_too_large_string(self):
        self.assertRaises(ValueError, calculate_factorial, "11")

    def test_string(self):
        self.assertRaises(TypeError, calculate_factorial, "s")

    def test_case_zero_integer(self):
        self._assert(0, 1)

    def test_case_zero_string(self):
        self._assert("0", 1)

    def test_larger_than_zero_integer(self):
        self._assert(7, 5040)

    def test_larger_than_zero_string(self):
        self._assert("7", 5040)