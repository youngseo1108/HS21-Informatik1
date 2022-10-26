'''
In this task you are going to practice black-box testing, thereby testing the program's ability to comply with its specification, 
in terms of expected output to specific inputs, with no knowledge about its implementation.

Function Specification
The function you will be testing, called fine_calculator calculates the cost of a traffic fine caused by speeding. 
The function takes 2 parameters
- Area: the area where the speed control is made. 
- Speed: the measured speed during the speed control. A fine is calculated depending on the area's type and the speed recorded.

There are 3 Area types: Urban, Expressway and Motorway. Each area has its own speed limit and a fine coefficient:
- The speed limit for Urban areas is 50 km/h, and the fine coefficient is 1
- The speed limit for Expressway areas is 100 km/h, and the fine coefficient is 0.8
- The speed limit for Motorway areas is 120 km/h, and the fine coefficient is 0.5

A correct implementation of fine_calculator must comply with the following requirements:
- For the speed parameter it expects a non-negative (float or int) number
- For the area parameter it expects a lowercase string 'urban', 'expressway' or 'motorway'
- The function returns the string Invalid Area Type if it receives an area parameter with the type other than string
- The function returns the string Invalid Area Value if it receives an string parameter other than the 3 areas defined above
- The function returns the string Invalid Speed Type if it receives a speed parameter with the type other than the defined above
- The function returns the string Invalid Speed Value if it receives an out of range speed parameter
- The function returns 0 if the speed provided to the function is less than the speed limit.
- If the measured speed exceeds the speed limit and the parameters are valid, the amount of the fine is calculated by multiplying the area fine coefficient by the square of the overspeed percentage, ie: fine_coefficient * overspeed_percentage²; see a concrete example below
- If the parameters are valid, the function returns the total fine amount to the closest integer value

For example, if the area parameter is given as motorway and the speed parameter is 180 km/h, 
the percentage of overspeed is 50% since Motorways' speed limit is 120 km/h. 
The amount of the fine is 0.5 x 50² = 1250, hence:
fine_calculator("motorway", 180) == 1250
'''
from unittest import TestCase
from script1 import fine_calculator

class FineCalculatorTest(TestCase):
    # returns 'Invalid Speed Value' 
    # if it receives an out of range speed parameter
    def test_speed_value(self):
        expected = 'Invalid Speed Value'
        actual = fine_calculator('urban', -1)
        self.assertEqual(actual, expected)

    # returns 'Invalid Area Type' if it receives 
    # an area parameter with the type other than string
    def test_area_type(self):
        expected = 'Invalid Area Type'
        actual = fine_calculator(1, 10)
        self.assertEqual(actual, expected)

    # returns the string Invalid Area Value if it receives 
    # an string parameter other than the 3 areas defined above
    def test_area_value(self):
        expected = 'Invalid Area Value'
        actual = fine_calculator('Urban', 10)
        self.assertEqual(actual, expected)

    # returns the string Invalid Speed Type if it receives 
    # a speed parameter with the type other than the defined 
    # above (non-negative int or float) 
    def test_speed_type(self):
        expected = 'Invalid Speed Type'
        actual = fine_calculator('urban', 8j)
        self.assertEqual(actual, expected)


    # return 0: urban
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

    def test_urban_speeding(self):
        expected = round(1 * ((90/50 - 1)*100)**2)
        actual = fine_calculator('urban', 90)
        self.assertEqual(actual, expected)

    def test_expressway_speeding(self):
        expected = round(0.8 * ((120/100 - 1)*100)**2)
        actual = fine_calculator('expressway', 120)
        self.assertEqual(actual, expected)

    def test_motorway_speeding(self):
        expected = round(0.5 * ((180/120 - 1)*100)**2)
        actual = fine_calculator('motorway', 180)
        self.assertEqual(actual, expected)

#---------------------solution--------------------------#
class SampleFineCalculatorTest(TestCase):
    coefficients = {
        "urban": 1,
        "expressway": 0.8,
        "motorway": 0.5
    }

    speed_limits = {
        "urban": 50,
        "expressway": 100,
        "motorway": 120
    }

    def calculate_expected(self, area, speed):
        speed_limit = self.speed_limits[area]
        if (speed <= speed_limit):
            return 0
        else:
            coefficient = self.coefficients[area]
            difference = speed_limit - speed
            difference_ratio = (difference / speed_limit)*100
            fine = coefficient * difference_ratio**2
            return round(fine)

    def _assert(self, area, speed):
        try:
            actual = fine_calculator(area, speed)
            expected = self.calculate_expected(area, speed)
        except Exception as e:
            self.fail("An unexpected error is raised")

        self.assertEqual(expected, actual)

    def test_01_return_type_valid(self):
        area = "urban"
        speed = 60
        actual = fine_calculator(area, speed)
        self.assertIsInstance(actual, int)

    # Urban area speed is lower than the limit of 50
    def test_02_urban_lower_limit(self):
        area = "urban"
        speed = 49
        self._assert(area, speed)

    # Urban area speed is on the limit of 50
    def test_03_urban_on_limit(self):
        area = "urban"
        speed = 50
        self._assert(area, speed)

    # Urban area speed is beyond the limit of 50
    def test_04_urban_beyond_limit_01(self):
        area = "urban"
        speed = 51
        self._assert(area, speed)

    # Urban area speed is beyond the limit of 50
    def test_05_urban_beyond_limit_02(self):
        area = "urban"
        speed = 100
        self._assert(area, speed)

    # Expressway area below the limit. Limit is 100
    def test_06_expressway_below_limit(self):
        area = "expressway"
        speed = 99
        self._assert(area, speed)

    # Expressway area speed is on the limit of 100
    def test_07_expressway_on_limit(self):
        area = "expressway"
        speed = 100
        self._assert(area, speed)

    # Expressway area speed is beyond the limit of 100
    def test_08_expressway_beyond_limit_01(self):
        area = "expressway"
        speed = 101
        self._assert(area, speed)

    # Expressway area speed is beyond the limit of 100
    def test_09_expressway_beyond_limit_02(self):
        area = "expressway"
        speed = 140
        self._assert(area, speed)

     # Motorway area below the limit. Limit is 120
    def test_10_motorway_below_limit(self):
        area = "motorway"
        speed = 119
        self._assert(area, speed)

    # Motorway area on the limit. Limit is 120
    def test_11_motorway_on_limit(self):
        area = "motorway"
        speed = 120
        self._assert(area, speed)

    # Motorway area beyond the limit. Limit is 120
    def test_12_motorway_beyond_limit_01(self):
        area = "motorway"
        speed = 121
        self._assert(area, speed)

    # Motorway area beyond the limit. Limit is 120
    def test_13_motorway_beyond_limit_02(self):
        area = "motorway"
        speed = 150
        self._assert(area, speed)

    # Urban area below the limit, float input
    def test_14_urban_below_limit_float(self):
        area = "urban"
        speed = 49.99
        self._assert(area, speed)

    # Urban area on the limit, float input
    def test_15_urban_on_limit_float(self):
        area = "urban"
        speed = 50.0
        self._assert(area, speed)

    # Urban area beyond the limit, float input
    def test_16_urban_on_beyond_float(self):
        area = "urban"
        speed = 150.01
        self._assert(area, speed)

    # Urban area invalid negative speed
    def test_17_invalid_speed_negative(self):
        area = "urban"
        speed = -3
        actual = fine_calculator(area, speed)
        expected = "Invalid Speed Value"
        self.assertEqual(actual, expected)

    # Urban area invalid string speed
    def test_18_invalid_speed_string(self):
        area = "urban"
        speed = "30"
        actual = fine_calculator(area, speed)
        expected = "Invalid Speed Type"
        self.assertEqual(actual, expected)

    # Invalid area with dict type
    def test_19_invalid_area_type_dict(self):
        area = ["urban"]
        speed = "30"
        actual = fine_calculator(area, speed)
        expected = "Invalid Area Type"
        self.assertEqual(actual, expected)

    # Invalid area with int type
    def test_20_invalid_area_type_int(self):
        area = 10
        speed = "30"
        actual = fine_calculator(area, speed)
        expected = "Invalid Area Type"
        self.assertEqual(actual, expected)

    # Invalid area with int type
    def test_21_invalid_area_value(self):
        area = "Zurich"
        speed = "30"
        actual = fine_calculator(area, speed)
        expected = "Invalid Area Value"
        self.assertEqual(actual, expected)
