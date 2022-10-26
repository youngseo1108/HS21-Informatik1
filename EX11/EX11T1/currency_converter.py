#!/usr/bin/env python3
# add imports, if necessary
from exchange_rates import*

def convert(amount, from_currency, to_currency):
    if to_currency in EXCHANGE_RATES[from_currency]:
        res = amount * EXCHANGE_RATES[from_currency][to_currency]
    else:
        res = amount / EXCHANGE_RATES[from_currency][to_currency]
    return res

# jpy -> gbp: 0.7 (= 7/10)
# gbp -> jpy: 

# gbp = jpy * exchange rate
# jpy = gbp/exchangerate