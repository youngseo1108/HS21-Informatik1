'''
Bakery
- initiated with a starting capital it can work with. 
- It can procure dough, produce bread out of the dough and finally sell the bread. 
- take_loan and pay_rent_and_loan.
- When a Bakery produces bread out of dough, it converts all the dough to bread & pays the cost for that.
- If the Bakery does not have enough capital to convert all the dough to bread, 
it converts as many doughs to bread as it can afford. A Warning should be raised in this case. 
- For improving the sale on the bread the Bakeries have a discount on the price_per_unit of 25%. 
- As the Bakeries are subsidized they only have to pay 80% of the rent in the pay_rent_and_loan function. 
- The function get_status is a helper function to check the status of Bakery and should return a tuple 
with the following elements in this order: capital, loan, interest, initial_loan_amount, dough, bread. 

b = Bakery(10000)
b.procure(1, 1000) 
b.get_status() # 9000, 0, 0, 0, 1000, 0
b.produce(1)
b.get_status() # 8000, 0, 0, 0, 0, 1000
b.sell(4, 1000)
b.get_status() # 11000, 0, 0, 0, 0, 0
b.pay_rent_and_loan(1000)
b.get_status() # 10200, 0, 0, 0, 0, 0

Note: The super keyword makes it easy to call a method defined by the parent type.
Note: An abstract base class extends ABC and adds the annotation @abstractmethod to abstract methods.
Note: You have to submit four files as solution: shop.py, bakery.py, clothing_store.py and shopping_center.py
'''
from shop import Shop


class Bakery(Shop):

    def __init__(self, capital):        
        # initiated with a starting capital it can work with
        # It can procure dough, produce bread out of the dough and finally sell the bread.
        super().__init__(capital)
        self.__loan = 0
        self.__interest = 0
        self.__initial_loan_amount = 0
        self.__dough = 0
        self.__bread = 0        

    def sell(self, price_per_unit, units):
        # For improving the sale on the bread the Bakeries have a discount on the price_per_unit of 25%. 
        # b.sell(4, 1000)
        # b.get_status() # 11000, 0, 0, 0, 0, 0
        pass

    def produce(self, costs_per_unit):
        '''When a Bakery produces bread out of dough,
        it converts all the dough to bread and pays the cost for that.
        If the Bakery does not have enough capital to convert all the dough to bread,
        it converts as many doughs to bread as it can afford. 
        A Warning should be raised in this case.
        '''
        pass

    def add_procured_units(self, units):
        self.__units = units
        '''
b = Bakery(10000)
b.procure(1, 1000) # dough 
b.get_status() # 9000, 0, 0, 0, 1000, 0
b.produce(1)
b.get_status() # 8000, 0, 0, 0, 0, 1000
b.sell(4, 1000)
b.get_status() # 11000, 0, 0, 0, 0, 0
b.pay_rent_and_loan(1000)
b.get_status() # 10200, 0, 0, 0, 0, 0
It can procure dough, produce bread out of the dough and finally sell the bread.
        '''
        pass

    def get_produced_units(self):
        pass

    def set_produced_units(self, units):
        pass

    def pay_rent_and_loan(self, rent):
        # pay 80% of the rent in the pay_rent_and_loan function.
        # b.pay_rent_and_loan(1000)
        # b.get_status() # 10200, 0, 0, 0, 0, 0
        self.__loan -= rent * 0.8

    def get_status(self):
        # a helper function to check the status of Bakery and should return a tuple with the following elements 
        # in this order: capital, loan, interest, initial_loan_amount, dough, bread. 
        return (self.__capital, self.__loan, self.__interest, self.__initial_loan_amount, self.__dough, self.__bread)

b = Bakery(10000)