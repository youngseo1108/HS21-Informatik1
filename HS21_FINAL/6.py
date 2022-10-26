'''
1. The class Student 
- represents a student which has a name and a school year. 
- The name should be passed to the constructor as a string; a new student always starts in school year number 1. 

Student should implement the following methods:
- learn should take no parameters and increase the school year of the student by 1.
- get_name and get_year should return the name and school year.

2. The class School
- represents a school. 
- A school has a name and can educate students of specific school years. 
- the constructor of School should take the name as a string, 
and a list of integers which indicates which school years the school can teach. 
- the school keeps track of how often any student has successfully been educated (0 at instantiation). 
- a class variable national_taught should store how many times in total a student has been successfully educated across all schools 
(0 at the beginning). 

School should implement the following methods: 
2.1 educate 
- take an object of type Student as a parameter. 
- If the student belongs to a school year that cannot be taught at this school, a ValueError should be raised.
- Otherwise, educate should call the learn method of the student with a probability of 9/10. If this happens, the number of successfully educated students at the school should be increased by 1 and the class variable should also be increased by 1.
2.2 get_taught 
- return the number of successful education attempts at this school.
'''
import random

class Student:
    def __init__(self, name):
        self.name = name
        self.year = 1

    def get_year(self):          
        return self.year
    
    def get_name(self):
        return self.name

class School:
    national_taught = 0
    def __init__(self, name, school_years):
        self.school_name = name # - the constructor of School should take the name as a string, and 
        self.school_years = school_years # a list of integers which indicates which school years the school can teach. 
        self.national_taught = School.national_taught
        School.national_taught += 1

    def educate(self, s):
        if s.get_year() not in self.school_years:
            raise ValueError
        learn_method = [False] + [True]*9
        choice = random.choice(learn_method)
        if choice == True:
            [s.get_year()].append(s.get_year()+1)

    def get_taught(self):
        return self.national_taught

# DO NOT SUBMIT THE LINES BELOW!
a = Student("Ueli")
assert a.get_name() == "Ueli"
assert a.get_year() == 1
s1 = School("Mätteliwise", [1,2,3,4,5,6])
s2 = School("Blüemlihof", [1,2,3,4,5,6])
assert s1.get_taught() == 0
## the following calls have random outcomes
s1.educate(a)
assert a.get_year() in [1, 2]
assert s1.get_taught() in [0, 1]
#s2.educate(a)
#assert a.get_year() in [1, 2, 3]
#assert s2.get_taught() in [0, 1]
#assert s2.national_taught in [0, 1, 2]