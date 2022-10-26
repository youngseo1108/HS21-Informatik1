'''
# TASK 1. Fine Calculator
fine_calculator
- calculates the cost of a traffic fine caused by speeding. 
- takes 2 parameters: Area and Speed. 
-> Area: area where the speed control is made
-> Speed: measured speed during the speed control. 
- A fine is calculated depending on the area's type and the speed recorded.

There are 3 Area types: Urban, Expressway and Motorway. Each area has its own speed limit and a fine coefficient:
- Urban: 50 km/h, and the fine coefficient is 1
- Expressway: 100 km/h, and the fine coefficient is 0.8
- Motorway: 120 km/h, and the fine coefficient is 0.5

A correct implementation of fine_calculator must comply with the following requirements:
- For the speed parameter, it expects a non-negative (float or int) number
- For the area parameter, it expects a lowercase string 'urban', 'expressway' or 'motorway'
- returns the string 'Invalid Area Type' if it receives an area parameter with the type other than string
- returns the string 'Invalid Area Value' if it receives an string parameter other than the 3 areas defined above
- returns the string 'Invalid Speed Type' if it receives a speed parameter with the type other than the defined above
- returns the string 'Invalid Speed Value' if it receives an out of range speed parameter
- returns 0 if the speed provided to the function is less than the speed limit.
- If the measured speed exceeds the speed limit and the parameters are valid, 
the amount of the fine = fine_coefficient * overspeed_percentage²
- If the parameters are valid, the function returns the total fine amount to the closest integer value
e.g. if the area parameter is given as motorway and the speed parameter is 180 km/h, the percentage of overspeed is 50% 
since Motorways' speed limit is 120 km/h. The amount of the fine is 0.5 x 50² = 1250, hence:

fine_calculator("motorway", 180) == 1250

Task details
Your task is to provide a good test suite in public/tests.py that can decide whether a given fine_calculator implementation follows the specification given above. Your test suite will be run with a variety of correct and incorrect implementations. The resulting grade depends on its ability to detect faulty implementations of fine_calculator. More specifically, the test suite should pass for a correct implementation and fail for an incorrect one.
Your task is to make sure that any implementation of fine_calculator does indeed always comply with all of specified requirements. For this purpose, you need to test the function with multiple test cases that you will write.

Note: You do not need to implement fine_calculator in public/script.py.
You can simply start writing your tests against unknown implementations. 
This is called "test-driven development": you provide the test suite first to specify the requirements for a given implementation 
by identifying interesting test cases. You then implement fine_calculator in script.py to run your test suite again 
using "Test & Run". However, your implementation of the function is irrelevant for the grading.

Note: You do not need to come up with good error messages, 
it is enough to fail a test if a problem can be detected (e.g., self.assertEquals(expected, actual)).

Note: Define your test suite as a subclass of TestCase. 
Do not use utility functions for the assertions, instead, include calls like self.assertEqual directly 
in the body of the test functions or the automated grading will mark the solution as incorrect.
'''
from unittest import TestCase
from unittest.case import expectedFailure
from script1 import fine_calculator

class FineCalculatorTest(TestCase):
# If the measured speed exceeds the speed limit and the parameters are valid, 
# the amount of the fine  = fine_coefficient * overspeed_percentage²
# If the parameters are valid, the function returns the total fine amount to the closest integer value

    # returns the string 'Invalid Area Type' if it receives an area parameter with the type other than string
    def test_area_type(self):
        expected = 'Invalid Area Type'
        actual = fine_calculator(1,1)
        self.assertEqual(actual, expected)
    
    # returns the string 'Invalid Area Value' if it receives an string parameter other than the 3 areas defined above
    # For the area parameter, it expects a lowercase string 'urban', 'expressway' or 'motorway'
    def test_area_value(self):
        expected = 'Invalid Area Value'
        actual = fine_calculator('Zurich', 90)
        self.assertEqual(actual, expected)

    # returns the string 'Invalid Speed Type' if it receives a speed parameter with the type other than the defined above
    def test_speed_type(self):
        expected = 'Invalid Speed Type'
        actual = fine_calculator('urban', 8j)
        self.assertEqual(actual, expected)

    # returns the string 'Invalid Speed Value' if it receives an out of range speed parameter
    # For the speed parameter, it expects a non-negative (float or int) number
    def test_speed_value(self):
        expected = 'Invalid Speed Value'
        actual = fine_calculator('urban', -10)
        self.assertEqual(actual, expected)

    # returns 0 if the speed provided to the function is less than the speed limit.
    def test_less_than_limit_urban(self):
        expected = 0
        actual = fine_calculator('urban', 50)
        self.assertEqual(actual, expected)

    # return 0: expressway
    def test_less_than_limit_expressway(self):
        expected = 0
        actual = fine_calculator('expressway', 100)
        self.assertEqual(actual, expected)

    # return 0: motorway
    def test_less_than_limit_motorway(self):
        expected = 0
        actual = fine_calculator('motorway', 120)
        self.assertEqual(actual, expected)

    # urban
    def test_urban_speeding(self):
        expected = 6400
        actual = fine_calculator('urban', 90)
        self.assertEqual(actual, expected)

    # expressway
    def test_expressway_speeding(self):
        expected = 320
        actual = fine_calculator('expressway', 120.0)
        self.assertEqual(actual, expected)
    
    # motorway
    def test_motorway_speeding(self):
        expected = 1250
        actual = fine_calculator('motorway', 180)
        self.assertEqual(actual, expected)


#print() # Invalid Area Value
#print() # Invalid Speed Type
#print() # Invalid Speed Value
#print()
#print()