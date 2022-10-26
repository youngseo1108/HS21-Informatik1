'''
Implement a class Person. Objects of this class should have three instance attributes: name, sex, and offspring. sex is a string, either "f" or "m", which can be optionally supplied in the constructor. If it's not supplied, sex should be assigned randomly upon instantiation. name is a string, which can be optionally supplied in the constructor. If no value is supplied, name should be None after instantiation. offspring should be an empty list after instantiation.

Person should implement a method mate_with, which takes one parameter of type Person. When called, this function should first compare the sex attributes of self and other. If they are identical, a ValueError should be raised. Otherwise, a new object of type Person should be instantiated without passing parameters to the constructor. The new object should be added to the offspring instance attribute of both self and other. Finally, the function should also return the newly instantiated object.

Implement __str__ and __repr__. Both functions should return the exact same value. If the attribute offspring of the instance is empty, the function should return a string like "NAME (SEX) has no children". If not, the following template should be used: "NAME (SEX) has N children: A, B, C, ...", where N is the number of objects in offspring and A, B, C, etc. are the name attributes of the objects in offspring. Note that if there's only one element, the word "child" should be used instead of "children". View the provided assertions for more valid examples of the string to be returned.

You can assume that constructors are only called with valid parameters.
'''
import random

class Person:
	pass

# DO NOT SUBMIT THE LINES BELOW!
#p1 = Person("Mark", "m")
#p2 = Person("Betty", "f")
#p3 = Person("John", "m")
#p4 = Person("Anna", "f")
#child = p1.mate_with(p2)
#assert(child.name == None)
#child.name = "Andrea"
#assert(len(p1.offspring) == 1)
#child = p3.mate_with(p2)
#assert(len(p2.offspring) == 2)
#child.name = "Terry"
#assert(p1.__str__() == "Mark (m) has 1 child: Andrea")
#assert(p2.__str__() == "Betty (f) has 2 children: Andrea, Terry")
#assert(p3.__repr__() == "John (m) has 1 child: Terry")
#assert(p4.__repr__() == "Anna (f) has no children")