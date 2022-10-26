'''
For this example, you need to know about "FizzBuzz": It's a 
simple counting game, where people sit in a circle and together,
one after another, count up from 1 to infinity (or at least until
they get bored or die of old age). However, every time a number is 
divisible by 3, a person will say "Fizz" instead of the number and 
every time a number is divisible by 5, they will say "Buzz". If a 
number is divisible by both 3 and 5, the person should say "FizzBuzz". 
So for example, the first couple of steps would be:

1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz,
16, 17, Fizz, 19, Buzz, Fizz, 22, 23, Fizz, Buzz, 26, Fizz, 28, 29, 
FizzBuzz, 31, 32, Fizz, 34, Buzz, Fizz, and so on...

Your task is to provide implementations for the two additional test cases:

1. test_five, should check that for n = 5, 
the function correctly returns "Buzz".
2. test_fifteen, should check that for n = 15, 
the function correctly returns "FizzBuzz".

You will notice that once you implement the fourth test case,
the test suite will fail, because the function is returning "Fizz"
instead of "FizzBuzz". 

3. Your final task is:
Fix the bug in the implementation of fizz_buzz() so that all tests
pass. If you want to run the test suite locally on your machine, 
make sure you are in the top-level directory of the exercise 
(which contains the public folder and description), and then run 
python -m unittest public/tests.py.

Alas, we may not yet have discussed imports, classes, "self" and
other aspects of the testing code, but you should be able to 
mentally "pattern-match" the important parts given the existing 
examples and comments. For future reference, have a look at the 
unittest Python module. In this exercise, we only used assertEqual,
but there are many more such functions, like assertTrue, 
assertGreater or assertAlmostEqual.
'''
# This enables us to write test cases.
# Imports will be discussed later in the lecture.
from unittest import TestCase

# For now, only the following import matters. It
# makes things from public/script.py available here.
from EX3 import script

# Don't worry about this line, for now it just
# marks the beginning of your Test Suite
class PublicTestSuite(TestCase):

    # These functions are the individual tests. You
    # can name them (almost) any way you like. In this
    # case, we decided to call this test "test_one".
    def test_one(self):
        # First, we set n in the script to 1
        script.n = 1
        # Then we call the fizz_buzz function
        # and assign the return value to "res"
        res = script.fizz_buzz()
        # Now we assert that res equals 1
        # If this were untrue, the assertion, and with
        # it the test, would fail.
        self.assertEqual(res, 1)

    # Another test to check if calling fizz_buzz()
    # with n = 3 will return "Fizz".
    def test_three(self):
        script.n = 3
        res = script.fizz_buzz()
        self.assertEqual(res, "Fizz")

    # Now, implement a third test case that checks if
    # given n = 5, the function correctly returns
    # "Buzz". The test is very similar to the second
    # test case and it should pass if you hit
    # "Test & Run". Do not rename this test!

    def test_five(self):
        script.n = 5
        res = script.fizz_buzz()
        self.assertEqual(res, 'Buzz')

    # Finally, implement a fourth test case that
    # checks if given n = 15, the function correctly
    # returns "FizzBuzz". Again, the test is very
    # similar to the others. You will notice that the
    # test will fail because of the existing bug in
    # fizz_buzz()! Do not rename this test.

    def test_fifteen(self):
        script.n = 15
        res = script.fizz_buzz()
        self.assertEqual(res, 'FizzBuzz')