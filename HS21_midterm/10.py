'''
Implement a function bill, which takes as parameters:

per_hour: a float representing the hourly rate of a worker, and
parts_prices_hours: a dictionary of the form {part: (price, hours)}, 
- part is the name of a part, 
- price is a float representing the price of that part, 
- hours is a float representing the total amount of hours needed to install that part. 
price and hours can be None for some entries in parts_prices_hours.

return a tuple with two items, 
where the first item represents the total cost of buying and installing all of the parts 
and the second item is a boolean, reporting whether some information was missing whilst computing the total cost. 

The cost for installing each individual part should be computed as: 
part_price + (parts_hours * per_hour) and the total cost is the sum of installing all parts. 

If the price of a part is None, a zero cost should be assumed for that part, 
and if hours, of a part is None one hour should be assumed. Consider the assert statements given below as examples for bill.
'''
def bill(per_hour, parts_prices_hours):
    # part_price + (parts_hours * per_hour)
    cost = 0
    missing = False
    for k in parts_prices_hours.keys():
        if parts_prices_hours[k][0] == None:
            cost += 0 + parts_prices_hours[k][1]*per_hour
            missing = True
        elif parts_prices_hours[k][1] == None:
            cost += parts_prices_hours[k][0] + 1*per_hour
            missing = True
        else:
            cost += parts_prices_hours[k][0] + parts_prices_hours[k][1]*per_hour
    return (cost, missing)

assert(bill(0, {'Door': (23.33, 2.50)}) == (23.33, False))
assert(bill(0, {}) == (0, False))
assert(bill(0, {'Door': (None, 3.0)}) == (0, True))
assert(bill(50, {'Door': (None, 3.0)}) == (150, True))
assert(bill(50, {'Door': (10, None)}) == (60, True))
assert(bill(10.5, {'Door': (None, 3.0), 'Window': (22.22, 0.5)}) == (58.97, True))
assert(bill(10.5, {'Window': (22.22, 0.5)}) == (27.47, False))
print(bill(10.5, {'Window': (22.22, 0.5)}))