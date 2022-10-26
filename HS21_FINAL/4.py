'''
Implement a function currency_converter, 
- takes three parameters: 
1. two strings src and dst, which represent the names of the source and destination currencies, 
2. a number rate which is the conversion rate. 

- return a function that takes the desired amount in the source currency as the only parameter 
- returns a string like X SRC is Y DST. 
- converted value should be rounded to two decimal places. 
'''


def currency_converter(src, dst, rate):
    def function(n):
        return f'{n} {src} is {round(n * rate, 2)} {dst}'
    return function
    
#def outer_func(who):
#    def inner_func():
#        print(f"Hello, {who}")
#    inner_func()
#outer_func("World!")

# DO NOT SUBMIT THE LINES BELOW!
assert currency_converter("EUR", "CHF", 1.1)(5) == "5 EUR is 5.5 CHF"
chf_to_jpy = currency_converter("CHF", "JPY", 123)
assert chf_to_jpy(1) == "1 CHF is 123 JPY"
assert chf_to_jpy(2) == "2 CHF is 246 JPY"
assert currency_converter("Peanuts", "Pinecones", 0.2)(50) == "50 Peanuts is 10.0 Pinecones"
assert currency_converter("Blemflarcks", "Coins", 0.0021)(333.3) == "333.3 Blemflarcks is 0.7 Coins"
#print(currency_converter("EUR", "CHF", 1.1, 5))