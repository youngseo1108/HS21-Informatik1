'''
Assume that you are writing the cashier software for an ice cream shop.
The shop offers two types of ice cream: vanilla and chocolate. An order always consists of 

a cone and any number of scoops.

To make your calculation logic extendable, all prices and the number of ordered scoops can be configured through variables 
(i.e., num_scoops_... and price_...). The total price of an order is calculated by a function called get_price. 
This last part of the implementation is missing. Your task is to complete the code.

Please make sure that your solution is self-contained within the get_price function.
'''

price_cone = 0.70
price_per_scoop_vanilla = 1.00
price_per_scoop_chocolate = 1.10

num_scoops_vanilla = 1
num_scoops_chocolate = 3

# Change the function below to calculate the total price this
# order. Note that your implementation should work with any
# specific value, so you can't just add up the raw numbers,
# you MUST use the VARIABLES defined above. Do not forget the
# cone!
def get_price():
    # You need to change the following line
    price = price_cone + num_scoops_chocolate * price_per_scoop_chocolate + num_scoops_vanilla * price_per_scoop_vanilla
    # You don't need to change the following line
    return price

get_price()