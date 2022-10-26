'''
The software company (SoftwareCompany) can employee two different kinds of workers (Worker). 
Every worker has a name. 

1.2 Programmer
Programmers (Programmer) are workers with a permanent contract. 
Programmers have a fixed annual salary. 
Furthermore, each new programmer should be created with a unique ID, which is an integer, counting up, 
starting at zero for the first programmer. 

1.3 Testers (Tester) are workers which are employed on an hourly basis. 
They have an hourly salary and work a fixed number of hours per month. 
Testers must receive a minimum wage. Testers do not have a unique ID.

For all kinds of workers it should be possible to get their monthly salary. For programmers, the monthly salary is calculated by dividing the annual salary by the number of months. For salary payments, there are 14 months in a year. For testers, the monthly salary is calcualted by multiplying the hourly salary by the number of hours worked per month.

When printing a programmer using Python's print function, 
the command line should display a string like "Salary: X (UNIQUE_ID)", 
where X denotes the monthly salary and UNIQUE_ID denotes the worker's unique identifier. 
When printing a tester, the command line should display "Salary: X (temp)", where X denotes the monthly salary.

1.4 A software company 
- has a name and any number of workers. 
- It should be possible to add workers to a software company. 
- It should be possible to calculate the total monthly staff cost of a software company, 
which is simply the sum of all salaries of all workers for a month.

Implementation instructions:
Fill in the missing class implementations in the provided template. Do not add any other top-level definitions! Observing the following:

The provided assertions contain essential information on how the required objects should behave (especially regarding constructor- and method parameters).
Specify super classes where necessary.
Add constructors, class variables and instance attributes where necessary.
When trying to create a tester with an hourly salary less than 9.4, a ValueError should be raised.
When trying to add a worker to a software company although it has already been added, a ValueError should be raised.
All instance attributes of workers should be private, but it should be possible to get the name of a worker and the unique ID of a programmer via methods. The name of a software company should be public, but any internal state to store the workers should be private.
Add the necessary methods and make sure to name them correctly according to the assertions.
Where one class inherits from another, ensure to put common functionality into the base class instead of duplicating it in sub classes.
'''
from abc import ABC, abstractmethod

class Worker(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def get_monthly_salary(self):
        pass

class Programmer(Worker):
    counter = 0

    def __init__(self, name, yearly_salary) -> None:
        super().__init__(name)
        self.yearly_salary = yearly_salary
        self.id = Programmer.counter
        Programmer.counter += 1

    def get_monthly_salary(self):
        return round(self.yearly_salary / 12, 2)

class Tester(Worker):
    def __init__(self, name, hourly_salary, hours_per_month):
        super().__init__(name)
        self.hourly_salary = hourly_salary
        self.hours_per_month = hours_per_month

class SoftwareCompany:
    def __init__(self, company_name):
        self.company_name = company_name
        self.workers = []
    
    def add_worker(self, staff):
        self.workers.append(staff)
    
    def get_monthly_staff_cost(self):
        total = 0
        for e in self.workers:
            total += e.get_monthly_salary()
        return total

# DO NOT SUBMIT THE LINES BELOW!
#e = SoftwareCompany("Velcrosoft")
#i1 = Programmer("Bob", 60000) # yearly salary
#i2 = Programmer("Alice", 75000) # yearly salary
#i3 = Tester("Taylor", 21.50, 15) # hourly salary, hours per month
#assert i1.get_name() == "Bob"
#assert i3.get_name() == "Taylor"
#assert i1.get_id() == 0
#assert i2.get_id() == 1
#assert i1.get_monthly_salary() > 4000
#assert i3.get_monthly_salary() == 322.50
#e.add_worker(i1)
#e.add_worker(i2)
#e.add_worker(i3)
#assert e.get_monthly_staff_cost() > 9000