'''
Implement a test class named MyTestSuite, 
which tests an unknown implementation of a function is_palindrome(x) via the blackbox testing principle. 
The function is specified as follows:

- is_palindrome takes a string as parameter x and determines if it is a palindrome. 
It returns True if yes, otherwise False. 
A palindrome is a word that can be read the same forwards and backwards. 
If x is not a string, a TypeError is raised. 
If x is less than 3 characters long, a ValueError is raised. 
The following assertions illustrate the usage of is_palindrome

    assert is_palindrome("maoam")
    assert is_palindrome("Was it a car or a cat I saw?")
    assert (not is_palindrome("I don't know"))
    
You should implement roughly 7 test methods to test individual deviations from this specification in an isolated manner. 
Please call the function in your test methods directly and without specifying a module, for example like this:

    self.assertTrue(is_palindrome("sugus"))
    
Do not add top-level statements, like imports. 
Your solution may only contain import unittest and your implementation of the test class MyTestSuite.
'''
import unittest

class MyTestSuite(unittest.TestCase):
    # If x is not a string, a TypeError is raised. 
    def test_input_type(self):
        self.assertRaises(TypeError, self.is_palindrome, 1)

    # If x is less than 3 characters long, a ValueError is raised. 
    def test_x_less_than_3(self):
        self.assertRaises(ValueError, self.is_palindrome, 'I')

    # check True
    def test_result_True_word(self):
        self.assertTrue(is_palindrome("sugus"))
    
    # check False
    def test_result_False(self):
        self.assertFalse(is_palindrome("I don't know"))

    # check True
    def test_result_True_sentence(self):
        self.assertTrue(is_palindrome("Was it a car or a cat I saw?"))