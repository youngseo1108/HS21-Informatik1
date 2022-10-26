from unittest import TestCase
from EX0803 import calculate_factorial

'''
2. 2nd part: White-box testing
White-box testing: implementing tests by studying the implementation of a program. In this part of the task you should write text cases for the function calculate_factorial only.
You should test whether the function calculate_factorial 
throws the correct exceptions 
when supplied with invalid inputs 
and you should also test whether it works normally with valid input. 
To check whether a function throws an exception, 
have a look at self.assertRaises. 
You do not have to test the error messages themselves. 
As your function also should accept integers, test these cases as well. 
And remember to also test edge cases!
Note: With self.fail() you can make a test case fail.
'''

class MyTests(TestCase):
    # return None if the input is None. 
    def test_input_none(self):
        actual = calculate_factorial(None)
        self.assertIsNone(actual)

    # If the input is a string, convert the input string into an integer
    # if not possible, throw a TypeError with the message "TypeError: string"
    def test_error_convert_str(self):
        with self.assertRaises(TypeError):
            calculate_factorial('a')

    # If the converted number or integer input is negative
    # -> throw a ValueError with the message "ValueError: number negative". 
    def test_error_negative_num(self):
        with self.assertRaises(ValueError):
            calculate_factorial(-1)

    # If the converted number or integer input is larger than 10
    # -> throw a ValueError but with the message "ValueError: number too large"
    def test_error_lager_than_10(self):
        with self.assertRaises(ValueError):
            calculate_factorial(11)

    # returns the factorial of the input inp as an integer.
    def test_cal_factorial(self):
        expected = 120
        actual = calculate_factorial(5)
        self.assertEqual(actual, expected)

#------------------solution--------------#
#!/usr/bin/env python3
# Sample Solution
import random

min_length_global = 1
max_length_global = 1
char_start_global = 65
char_end_global = 65

def fuzzer(min_length, max_length, char_start, char_end):
    string = ""
    string_length = random.randrange(min_length, max_length + 1)
    for _ in range(0, string_length):
        string += chr(random.randrange(char_start, char_end + 1))
    return string


def calculate_factorial(inp):

    if inp is None:
        return None
    try:
        inp = int(inp)
    except:
        raise TypeError("TypeError: string")

    if inp < 0:
        raise ValueError("ValueError: number negative")

    if inp > 10:
        raise ValueError("ValueError: number too large")

    if inp == 0:
        return 1
    factorial = 1
    for i in range(1, inp + 1):
        factorial *= i
    return factorial


def run(trials):
    l = []
    for _ in range(trials):
        inp = fuzzer(min_length_global, max_length_global, char_start_global, char_end_global)
        try:
            calculate_factorial(inp)
        except ValueError as e:
            l.append((1, str(e)))
        except:
            l.append((1, "Other error"))
        else:
            l.append((0, ""))
    return l
