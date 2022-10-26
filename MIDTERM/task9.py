'''
Implement a function russian_roulette, 
which reflects the first round of a game of russian_roulette. 
It takes no parameters and returns a string.
The function, when called, should have a 1 in 6 chance of 
returning "BANG!!!" and a 5 in 6 chance of returning "Click!". 
Hint: You will need to use the random module.
'''
# russian_roulette(), when called several times, should return 
# "BANG!!!" 1/6th of the time, and "Click!" 5/6th of the time
import random

def russian_roulette():
    if random.randint(1,6) == 1:
        return 'BANG!!!'
    else:
        return 'Click'

print(russian_roulette())
print(russian_roulette())
print(russian_roulette())
print(russian_roulette())
print(russian_roulette())
print(russian_roulette())