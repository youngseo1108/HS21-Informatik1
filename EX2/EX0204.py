'''
You have learned in the lecture how to use the string slicing operator to 
select substrings from a given string. Strings also have very useful methods,
like find, which can be used to find the index of a particular character in 
a string (e.g., "abc".find("b") would result in 1), or the methods upper()
or lower() that can transform a string to its uppercase/lowercase variants
(e.g., "aBc".upper() would result in "ABC"). You can also get the length of
any string as an integer number by calling the len() function on the string
(e.g., len("xYz") would return 3).

You can find all necessary information on these functions in the 
Python API: https://docs.python.org/3.8/library/stdtypes.html#string-methods

In this exercise, you will receive a non-empty string s as input, which 
will always contain exactly one colon (:). 
Write a program that takes such a string and transforms all characters 
before the colon to lowercase and all characters after the colon to 
uppercase. For example, the string "aB:cD" should be transformed into "ab:CD".
The value should be returned by the transform_string() function. 
Of course, your program should work for arbitrary input strings s, as 
long as they contain a colon, so they could have any number of characters 
before or after the colon.
'''

#!/usr/bin/env python3

s = "aB:cD"

# perform the transformation
def transform_string():
    # Insert your code here.
    # You may want to use several variables to
    # store temporary values (such as the index of
    # the colon or the two strings before and after
    # it). Then, you can construct the final result
    # from your temporary variables.
    idx = s.find(':')
    res = s[:idx].lower() + s[idx:].upper()
    # You don't need to change the following line.
    # It simply returns the string created above.
    return res
    
print(transform_string())