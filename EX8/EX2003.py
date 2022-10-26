'''
1. Fuzz testing
Fuzzing is the process of generating random inputs to feed into a program 
with the goal of hopefully uncovering unexpected behavior without having to guess corner cases. 
Many bugs stem from errors of the input processing, so by supplying many random inputs, these bugs may be uncovered automatically.

This task shows a simple application of a fuzzer and runner which are both represented as functions named fuzzer and run. 
The runner tests the program calculate_factorial with random input from the fuzzer function.

Your task is to implement these three functions:
1.1 fuzzer 
- takes four input parameters (all integers) 
- and returns a string of random length containing random characters. 
- The first two parameters min_length and max_length determine how long the returned random string can be. 
- The two parameters char_start and char_end determine which character from the ASCII table should be included in the returned random string. 
fuzzer(5, 10, 43, 57) == .5728//
a string between 5 and 10 (including) characters long and contains randomly selected characters 
corresponding to decimal numbers between 43 (+) and 57 (9) from the ASCII table. 

1.2 calculate_factorial 
- takes one input parameter inp (an integer or a string) 
- returns the factorial of the input inp as an integer. 
- return None if the input is None. 
- If the input is a string, the function should try to convert the input string into an integer 
- and if this is not possible, the function should throw a TypeError with the message "TypeError: string". 
- If the converted number or integer input is negative, 
the function should throw a ValueError with the message "ValueError: number negative". 
- If the converted number or integer input is larger than 10, the function should also throw a ValueError but with the message "ValueError: number too large". This is for example a simulation of a buffer overflow.

1.3 run 
- has one input parameter trials (an integer) 
- and returns a list of tuples, containing feedback on executing the calculate_factorial function with random inputs. 
- should run your function calculate_factorial as many times as specified in trials. 
- Each time calculate_factorial is run, it should be provided with a new random input obtained by calling the fuzzer function. 
- For the parameter input for the function fuzzer use the provided global variables instead of passing values directly to the function. 
- For each run, a new tuple should be appended to the return value, where each tuple consists of two elements. The first element is an integer which can be 0 (success) or 1 (failure) and the second element contains a string. When calculate_factorial throws a ValueError, the error should be caught and a tuple with the elements 1 and the error message should be added to the list which will be returned. For example if calculate_factorial raises an ValueError with the message "ValueError: number too large", the following tuple should be added to the list: (1, "ValueError: number too large"). Any other thrown error should be caught and a tuple with the elements 1 and the string "Other error" should be added to the list. If no error is thrown, a tuple with the elements 0 and an empty string should be added to the list. If no element is added to the resulting list, an empty list should be returned.

Note: For the building a string of random range and with random characters these functions can help: randrange, chr
Note: Check out the lecture slides for raising and catching Errors/Exceptions.

White-box testing
White-box testing is about implementing tests by studying the implementation of a program. In this part of the task you should write text cases for the function calculate_factorial only.

You should test whether the function calculate_factorial throws the correct exceptions when supplied with invalid inputs 
and you should also test whether it works normally with valid input. 
To check whether a function throws an exception, have a look at self.assertRaises. 
You do not have to test the error messages themselves. 
As your function also should accept integers, test these cases as well. And remember to also test edge cases!

Note: With self.fail() you can make a test case fail.
'''
import random

min_length_global = 0
max_length_global = 5
char_start_global = 30
char_end_global = 65

def fuzzer(min_length, max_length, char_start, char_end):
    res = ''
    length = random.randrange(min_length, max_length+1)
    while len(res) < length:
        res += chr(random.randrange(char_start, char_end+1))
    return res

def calculate_factorial(inp):
    # return None if the input is None. 
    if inp == None:
        return None

    # If the input is a string, the function should try to convert the input string into an integer 
    try:
        inp = int(inp)
    # if this is not possible, the function should throw a TypeError with the message "TypeError: string".
    except:
        raise TypeError('TypeError: string')
    # If the converted number or integer input is negative, the function should throw a ValueError with the message "ValueError: number negative". 
    if inp < 0:
        raise ValueError('ValueError: number negative')
    # If the converted number or integer input is larger than 10, 
    # the function should also throw a ValueError but with the message "ValueError: number too large". 
    # This is for example a simulation of a buffer overflow.
    if inp > 10:
        raise ValueError('ValueError: number too large')
    
    res = 1
    for i in range(1, inp+1):
        res *= i
    return res

def run(trials):
    l = []
    i = trials
    while i > 0:
        input = fuzzer(min_length_global, max_length_global, char_start_global, char_end_global)
        try:
            calculate_factorial(input)
        except ValueError as e:
            l.append((1, str(e)))
        except:
            l.append((1, 'Other error'))
        else:
            l.append((0, ''))
        i -= 1
    return l


#print(run(10))

#print(ord('A'))
#print(ord('z'))
#print(chr(30))
#print(chr(65))
#print(fuzzer(5, 10, 43, 57))
print(calculate_factorial(0))