'''
The root of the hierarchy is the base class Restaurant. 
This class provides basic functionality that pertain to all Restaurant types. 
Instances of Restaurant, Restaurants are initiated with a name and the cuisine_type offered (both strings). 
is_open is an optional parameter that defines whether the restaurant is already open at time of initialization. 

The class provides the following methods:

- describe_restaurant() returns a description of the restaurant as a string, containing the restaurant's name and the cuisine_type.
- open_restaurant(), sets a dedicated private instance variable to True.
- close_restaurant(), sets this instance variable to False.
- is_open() returns this instance variable.
- add_consumption_unit(name, price) adds an offer with a name and corresponding price to the restaurants menu.
- remove_consumption_unit(name) removes the offer name from the menu.
- get_menu() should return a dictionary mapping unit names to prices. Make sure that get_menu() returns a copy, such that the dictionary cannot be adapted from the outside. Use copy.deepcopy(dictionary) for this (import already provided).
- sell_unit(name) adds the price of the sold unit name to an instance variable for sales. If the restaurant is not open already, this should raise a Warning().
- get_sales() returns the sum of all the prices of sold units.

Restaurant has two direct subtypes, OnsiteRestaurant and DeliveryRestaurant. 
While both are restaurants, they handle specific logic that goes further than the one from the Restaurant class.
'''
import copy

class Restaurant:

    def __init__(self, name, cuisine_type, is_open = False):
        self.__name = name
        self.__cuisine_type = cuisine_type
        self.__is_open = is_open
        self.__menu = {}
        self.__sold_unit = 0

    def describe_restaurant(self):
        return f'{self.__name}: {self.__cuisine_type}'

    def open_restaurant(self):
        self.__is_open = True

    def close_restaurant(self):
        self.__is_open = False

    def is_open(self):
        return self.__is_open

    def add_consumption_unit(self, name, price):
        # adds an offer with a name and corresponding price 
        # to the restaurants menu.
        self.__menu[name] = price

    def remove_consumption_unit(self, name):
        # remove_consumption_unit(name) removes the offer name 
        # from the menu
        del self.__menu[name]

    def get_menu(self):
        # return a dictionary mapping unit names to prices. 
        # Make sure that get_menu() returns a copy, 
        # such that the dictionary cannot be adapted from the 
        # outside. Use copy.deepcopy(dictionary) for this 
        # (import already provided).
        return copy.deepcopy(self.__menu)

    def sell_unit(self, name):
        # adds the price of the sold unit name to an instance 
        # variable for sales. If the restaurant is not open 
        # already, this should raise a Warning().
        if self.__is_open == True:
            self.__sold_unit += self.__menu[name]
        else:
            raise Warning(f'{self.__name} is not opened.')

    def get_sales(self):
        # get_sales() returns 
        # the sum of all the prices of sold units.
        return self.__sold_unit