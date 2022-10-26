'''
# TASK 3. Restaurant
[Restaurant]
- used to instantiate a restaurant object. 
- A restaurant object holds its own name, menu and places orders. 
- returns the total revenue of its orders and other attributes it holds, if requested. 

1. parameters: name and menu_list.
- name: a string carrying the name of the restaurant
- menu_list: a list of Item objects that are available in the restaurant

# A restaurant instance with name Zurich_1 and 1 item menu list of Hamburger at 20 CHF.
Restaurant("Zurich_1", [Item("Hamburger", 20)])

2. Functions
2.1 get_restaurant_name: return a string carrying the name of the restaurant instance
2.2 get_menu_list: return the menu (ie. the list of Item objects) of the restaurant instance
2.3 get_order_list: return the string No order yet if no orders have been placed in the restaurant instance yet. 
Otherwise it should return the list of orders placed at the restaurant instance.
2.4 set_order: create an Order object with the provided list of Item objects and should update the order list of the restaurant instance. Only items that can be found in the restaurant menu can be added to an order. Other items provided by the customer should be discard by the function.
2.5 get_revenue: return the revenue of the restaurant instance. 
It is the sum of all order bills placed in the restaurant. If no order has been placed yet, the function should return 0.


[Order]
accepts an item_list as an argument. 
item_list is a list containing the objects instantiated from the Item class. 
The Order object holds the total price of the given order and the list of products in the order. 
The function get_bill_amount returns the bill amount of that particular order instance. 
__repr__ function is used to represent the object as string.

[Item]
Products are instantiated from the Item class with 2 parameters : name and price. The name attribute is a string holding the name of the product, and price attribute holds the price of the product. The object has functions to return it's attributes.

Example
    hamburger = Item("Hamburger", 20)
    pizza = Item("Pizza", 35)
    steak = Item("Steak", 50)
    menu_list = [hamburger, pizza]
    restaurant_name = "Zurich_1"
    restaurant = Restaurant(restaurant_name,  menu_list)
    order_list = [pizza, pizza, hamburger, steak]
    restaurant.set_order(order_list)
    restaurant.get_revenue() # ==> Returns 90
'''

from item import Item
from order import Order

class Restaurant:

    def __init__(self, restaurant_name, menu_list):
        self.__restaurant_name = restaurant_name
        self.__menu_list = menu_list

    def get_restaurant_name(self):
        '''return a string carrying the name of the restaurant instance'''
        return self.__restaurant_name

    def get_menu_list(self):
        '''return the menu (ie. the list of Item objects) of the restaurant instance'''
        return self.__menu_list

    def get_order_list(self):
        '''return the string No order yet if no orders have been placed in the restaurant instance yet. 
        Otherwise it should return the list of orders placed at the restaurant instance.'''
        if len(self.__item_list) == 0:
            return 'No order yet'
        return self.__item_list

    def set_order(self, item_list):
        '''create an Order object with the provided list of Item objects and should update the order list of the restaurant instance. 
        Only items that can be found in the restaurant menu can be added to an order. 
        Other items provided by the customer should be discard by the function.'''
        self.__item_list = []
        for e in item_list:
            if e in self.__menu_list:
                self.__item_list.append(e)
        return self.__item_list

    def get_revenue(self):
        '''return the revenue of the restaurant instance. 
        It is the sum of all order bills placed in the restaurant. If no order has been placed yet, the function should return 0.'''
        total = 0
        for menu in self.__item_list:
            total += menu.get_item_price()
        return total

# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    # Create Item Objects with Name and Price
    steak = Item("Steak", 25)
    salad = Item("Salad", 10)
    fish = Item("Fish", 30)
    pizza = Item("Pizza", 40)
    # Create menu list
    menu_list = [steak, salad, fish]
    # Create order list
#    order_list = [steak, steak, salad, pizza]
    order_list = []
    # Create restaurant object with name and menu list
    restaurant = Restaurant("Zurich_1", menu_list)
    # Create an order with the order list
    print(restaurant.set_order(order_list))
    print(restaurant.get_order_list())
    # Get the revenue of the restaurant object
    print(restaurant.get_revenue())
