'''
You've been tasked with programming an accounting system for a liquor store. This task description consists of three parts:

A specification of the relevant concepts and processes.
Complementary implementation instructions.
A code template (above) containing pre-defined classes which have to be implemented.
Please read all three parts carefully for a comprehensive specification. Once you have a clear picture of what to do, implement the necessary classes and tests. Finally, submit your solution.

Watch the clock or set an alarm! You must ensure that you have enough time to copy and submit your solution, before the exam ends! You can hand in your solution even if it is incomplete. Just make sure that your submission does not contain syntax- or other basic errors.

Conceptual description
The liquor store sells the following products: bottles and crates. Bottles are products with a fixed price and name. Crates are products which consist of multiple bottles. A new crate starts out without any bottles, so it should be possible to add individual bottles to the crate, up to a maximum of 20 bottles. It should also be possible to determine for a crate how many bottles it contains.

Both bottles and crates are products. For any product, it should be possible to get its price.

The price of a normal crate is calculated from the total price of all the bottles it contains. However, the liquor store also sells two special kinds of crates:

A fixed-price crate has a pre-determined price which is set when first creating it. The price remains independent from the number of bottles in the crate.
A discount crate has a price which is determined using the following strategy: for every additional bottle, get 2% off the crate (up to a maximum of 25% off, final price rounded to two decimal places). For example, a discount crate consisting of three bottles with a total price of 10.00 costs only 9.40, and a discount crate consisting of five bottles with a total price of 20.00 costs only 18.00.
Implementation instructions:
Fill in the missing class implementations in the provided template. Do not add any other top-level definitions! Observing the following:

Specify super classes where necessary.
Add constructors and instance attributes where necessary.
Data attributes of Bottle should be public, but any data attribute you might use inside Crate should be private.
Add the necessary methods.
Read the provided assertions for further hints on how the required objects should behave (specifically, their constructor parameters and methods).
Where one class inherits from another, ensure to put common functionality into the base class instead of duplicating it in sub classes.
Furthermore, implement three tests which cover the most important features:

test_crate_max_size should assert that add raises a RuntimeError if the crate capacity would be exceeded.
test_crate_price should assert that the price of a normal crate is calculated correctly.
test_discount_crate_price should assert that the price for discount crates is calculated correctly.
Template
Do not add additional classes! The top-level scope of your submission may ONLY contain class definitions and import statements, nothing else!
Do not change the pre-defined class and function names!
Your solution must be compatible with the pre-defined assertions; so take care when naming your methods!
'''
from abc import ABC, abstractmethod
import unittest

class Product:
	pass

class Bottle:
	pass

class Crate:
	pass

class DiscountCrate:
	pass

class FixedPriceCrate:
	pass

class ShopTestSuite(unittest.TestCase):

	def test_crate_add(self):
		c = Crate()
		c.add(Bottle(4.50, "Light Beer"))
		self.assertEqual(c.get_size(), 1)

	def test_crate_max_size(self):
		pass

	def test_crate_price(self):
		pass

	def test_discount_crate_price(self):
		pass

# DO NOT SUBMIT THE LINES BELOW!
#bottles = [Bottle(3.50, "Light Beer"), Bottle(4.50, "Passable Wine")] + 3 * [Bottle(4.00, "Strong Stuff")]
#assert(bottles[0].get_price() == 3.50)
#
#c = Crate()
#for b in bottles: c.add(b)
#assert(c.get_size() == 5)
#assert(c.get_price() == 20.00)
#
#c = FixedPriceCrate(11.11)
#for b in bottles: c.add(b)
#assert(c.get_price() == 11.11)
#
#c = DiscountCrate()
#for b in bottles: c.add(b)
#assert(c.get_price() == 18.00)
#
#unittest.main()