'''
재연습 필요
You are programming the cashier's system for a hot-dog stand with a menu as shown below. 
However, you offer some special discounts if certain conditions apply:

-When ordering a Water with a Spicy-Dog, the Water is free. 
This applies for every pair of these products ordered even if ordering multiple pairs.
-Every 6th beer in an order is free.

Implement a function bill which takes one parameter, order, 
which is a dictionary mapping product names to the number of each item ordered. 
- The function should return the total sum of the order. 
- The function should return 0 for an empty order. 
- The menu and pricing is provided as a dictionary menu.

Note that your solution must also work if the menu prices are adjusted. 
Don't use concrete values in your solution, but reference the prices in menu instead.
'''
menu = {
 "Hot Dog": 3.50,
 "Spicy Dog": 4.00,
 "Vegan Dog": 3.50,
 "Water": 1.50,
 "Fizzy Drink": 2.50,
 "Beer": 4.00
}

# bill({"Spicy Dog": 2, "Water": 3, "Beer": 8}) should return 37.5
# --> 37.5 = (2*4.00 + 3*1.50 - 2*1.50 + 8*4.00 - 1*4.00)
# --> 2 waters and one beer are free in this order
def bill(order):
    total = 0
    # total sum without discounts
    for item, count in order.items():
        total += count * menu[item]
    # subtract discount for waters
    if "Spicy Dog" in order and "Water" in order:
        free = min(order["Spicy Dog"], order["Water"])
        total -= free * menu["Water"]
    # subtract every 6th beer
    if "Beer" in order:
        free = order["Beer"] // 6
        total -= free * menu["Beer"]
    return total

print(bill({"Spicy Dog": 2, "Water": 3, "Beer": 8}))
print(bill({}))