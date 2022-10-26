'''
For this example, you need to know about "FizzBuzz": 
It's a simple counting game, where people sit in a circle and together, one after another, count up from 1 to infinity 
(or at least until they get bored or die of old age). 
However, every time a number is divisible by 3, a person will say "Fizz" instead of the number 
and every time a number is divisible by 5, they will say "Buzz". 
If a number is divisible by both 3 and 5, the person should say "FizzBuzz". 

So for example, the first couple of steps would be:
1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, 16, 17, Fizz, 19, Buzz, Fizz, 22, 23, Fizz, Buzz, 26, Fizz, 28, 29, FizzBuzz, 31, 32, Fizz, 34, Buzz, Fizz, and so on...

Be sure you understand the game!

The script implements a function fizz_buzz() which is supposed to return the correct word depending on the value of the variable n. 
It may look fine, but it actually contains a bug! But don't change the script yet.

Instead, have a look at public/tests.py and carefully read the comments. 
You will see that we already implemented two test cases, which cover n = 1 and n = 3. 
If you "Test & Run" the example without any modifications, both tests pass and everything seems fine. 
(The other two tests also pass, because they don't implement any checks - they just do a pass, which always gives a positive test result.)

Your task is to provide implementations for the two additional test cases:
- The third test case, test_five, should check that for n = 5, the function correctly returns "Buzz".
- The fourth test case, test_fifteen, should check that for n = 15, the function correctly returns "FizzBuzz".

You will notice that once you implement the fourth test case, the test suite will fail, 
because the function is returning "Fizz" instead of "FizzBuzz". Your final task is:

- Fix the bug in the implementation of fizz_buzz() so that all tests pass.

Alas, we may not yet have discussed imports, classes, "self" and other aspects of the testing code,
but you should be able to mentally "pattern-match" the important parts given the existing examples and comments.
'''
n = 0

def fizz_buzz():
    if n % 3 == 0 and n % 5 != 0:
        return "Fizz"
    elif n % 5 == 0 and n % 3 != 0:
        return "Buzz"
    elif n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    else:
        return n

print(fizz_buzz()) # n = 3
print(fizz_buzz()) # n = 5
print(fizz_buzz()) # n = 15
print(fizz_buzz()) # n = 2