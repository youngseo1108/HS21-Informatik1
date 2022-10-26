#!/usr/bin/env python3
'''
A ShoppingCenter is initiated with a starting capital and Shops. 
The shops should be passed as a list of shops. 
As a Bakeries and Clothing_Stores are of type Shop, 
both of them count as Shop. 
If a ShoppingCenter is initialized without a shop, 
a Warning should be raised. 
A ShoppingCenter can add a single shop with add_shop and remove a single shop with remove_shop. 
Remove_shop should return the Shop which was removed.

A ShoppingCenter can also grant a loan with grant_loan and collect rent and loan with collect_rent_and_loan. 
The function grant_loan has the following three parameters: shop, interest and amount. 
If a ShoppingCenter tries to grant a loan to a Shop which does not belong to the ShoppingCenter, 
grant_loan should raise a Warning. 
If the capital of the ShoppingCenter is not enough to grant the amount of the loan, 
grant_loan should also raise a Warning. When a loan is granted, 
the amount of the loan should be deducted from capital of the company 
and should be added to the loan state of the Shop. You should use take_loan for this. 
A ShoppingCenter also keeps track of its debtors within a list.
The collect_rent_and_loan has one parameter the rent which should be collected from the individual stores 
of the ShoppingCenter and added to the ShoppingCenter's capital. 
The function pay_rent_and_loan of Shop returns the amount a shop should pay in rent and loan 
and helps to fulfill the requirements of the collect_rent_and_loan. 
If the loan of a Shop hit 0 it should be removed from the list of debtors in the function collect_rent_and_loan.

Also implement the len function 
which should return the number of shops a shopping center 
has.

The function get_status is a helper function to check the status of a ShoppingCenter 
and should return a tuple with the following elements in this order: capital, 
shops, debtors. Shops and debtors should also be tuples which contain Shops. 
An example of a return for get_status could be the following: 
(10000, (bakery1, bakery2, clothing_store1), (bakery1, clothing_store1)). 
These are the states a ClothingSore should have.

bakery = Bakery(1000)
s = ShoppingCenter(10000, [bakery_two]) # (capital, shops, debtors) = (10000, (bakery,), ())
clothing_store = ClothingStore(2000)
s.add_shop(clothing_store) # (10000, (bakery, clothing_store), ())
s.grant_loan(bakery, 0.05, 1000) # (9000, (bakery, clothing_store), (bakery,))
s.collect_rent_and_loan(100) # (9330, (bakery, clothing_store), (bakery,))
'''
class ShoppingCenter:

    def __init__(self, capital, shops):
        self.__capital = capital
        if type(shops) != list:
            raise Warning('Cannot be initialized without shops')
        self.__shops = shops

    def collect_rent_and_loan(self, rent):
        pass

    def grant_loan(self, shop, interest, amount):
        pass

    def add_shop(self, shop):
        pass

    def remove_shop(self, shop):
        pass

    def get_status(self):
        #capital, shops, debtors. 
        # Shops and debtors should also be tuples which contain Shops. 
        # (10000, (bakery1, bakery2, clothing_store1), (bakery1, clothing_store1)). 
        pass

    def __len__(self):
        return len(self.__shops)