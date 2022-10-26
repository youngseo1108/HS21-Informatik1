'''
A ClothingStore is initiated with a starting capital it can work with. 
It can procure clothing_pieces and sell these clothing_pieces. 
Furthermore, a ClothingStore can also take_loan and pay_rent_and_loan. 
A ClothingStore can get a quantity discount of 20% when it procures more than 10 units. 
The function get_status is a helper function to check the status of ClothingStore 
and should return a tuple with the following elements in this order: 
capital, loan, interest, initial_loan_amount, clothing_pieces.
These are the states a ClothingStore should have. Have a look at the following example to get a better understanding 
of the ClothingStore class.

c = ClothingStore(10000)
c.procure(1, 1000) 
c.get_status() # 9200, 0, 0, 0, 1000
c.sell(4, 1000)
c.get_status() # 13200, 0, 0, 0, 0
c.pay_rent_and_loan(1000)
c.get_status() # 12200, 0, 0, 0, 0
'''
from public.shop import Shop

class ClothingStore(Shop):

    def __init__(self, capital):
        super.__init__(capital)
        self.__loan = 0
        self.__interest = 0
        self.__initial_loan_amount = 0
        self.__clothing_pieces = 0

    def procure(self, price_per_unit, units):
        pass

    def add_procured_units(self, units):
        pass

    def get_produced_units(self):
        pass

    def set_produced_units(self, units):
        pass

    def get_status(self):
        #capital, loan, interest, initial_loan_amount, clothing_pieces
        return (self.__capital, self.__loan, self.__interest, self.__initial_loan_amount, self.__clothing_pieces)