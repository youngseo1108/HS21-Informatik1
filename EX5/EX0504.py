'''
# TASK 4. Juliets Number
Task - Repeting for loops, indices and most common list operations
Your job in this task is to help Romeo by writing a program that 
- generates all possible phone numbers given an incomplete number, 
- and and then returns only those for which an account exists on Whatsapp.

For this you may adhere to the following specification:

get_possible_nrs(n)
- accepts a number as a string n, where one digit is missing (9 instead of 10 digits of a valid Swiss phone number).
- returns a list of whatsapp number strings that might belong to juliet.
- A number that may belong to juliet contains exactly one digit more than n (10 digits).
- This single digit may be at any index within n
- A list of possible Whatsapp numbers is stored in the list wa_nrs. 
Compare your generated numbers with the numbers in wa_nrs to keep only those which exist in Whatsapp.

# Hints
- Visualize where/at what indices a single digit could be inserted 
in a given test number
- Think about which python constructs you need to populate a list 
and check for list inclusion
'''
wa_nrs = ["0781111119", "0792653913", "0797763139", "0792793193", "0781139022", "0764320165"]
#len(wa_nrs)

# 0을 index마다 넣고 비교?!


# METHOD 1 (제출은 이걸로 함. 3/3)
from difflib import SequenceMatcher
#s_1 = "0781111119"
#s_2 = "076432165"
#s_3 = "0764320165"
#print(SequenceMatcher(a = s_1, b = s_2).ratio())
#print(SequenceMatcher(a = s_2, b = s_3).ratio())
#0.909090909091

def get_possible_nrs(n): # n = string
    possible_nrs_for_juliet = []
    # This single digit may be at any index within n
    # compare numbers with the existing list -> 9개의 숫자가 일치 -> append to the list
    #n_copy = n + '0'
#    counter = 10
    for i in range(len(wa_nrs)):
        if SequenceMatcher(a = n, b = wa_nrs[i]).ratio() > 0.9:
            possible_nrs_for_juliet.append(wa_nrs[i])
    return possible_nrs_for_juliet
# For this particular number, the function should find the last element in wa_nrs
print(get_possible_nrs("076432165"))
print(get_possible_nrs("077342119"))
# The expected phone numbers are 
# ['0779266313', '0789266313', '0792566313', '0792646313', 
# '0792663113', '0792663130', '0792663213', '0792663313', 
# '0792696313', '0796266313'] 
# but ['0792663113', '0792663130', '0792663213', '0792663313'] 
# have been found.

# ['0792653913', '0797763139', '0792793193', '0781139022', '0764320165']

#print(len(['0779266313', '0789266313', '0792566313', '0792646313', '0792663113', '0792663130', '0792663213', '0792663313', '0792696313', '0796266313']))
#print(len(['0792653913', '0797763139', '0792793193', '0781139022', '0764320165']))

# METHOD 2 
def get_possible_nrs(n): # n = string
    possible_nrs_for_juliet = []
    n_copy = n + '0'
    counter = 10
    for i in range(len(wa_nrs)):
        for j in range(10):
            for k in range(9):
                if wa_nrs[i][j] == n_copy[k]:
                    counter -= 1
        if counter < 2:
            possible_nrs_for_juliet.append(wa_nrs[i])
        counter = 0
    return possible_nrs_for_juliet

print(get_possible_nrs("076432165"))
print(get_possible_nrs("077342119"))
