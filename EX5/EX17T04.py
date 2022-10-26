'''
Task - Repeting for loops, indices and most common list operations

Your job in this task is to help Romeo by writing a program that produces all possibilities of phone numbers 
and provides him a list of possble numbers that are linked on Whatsapp. For this you may adhere to the following specification:
- Valid numbers have 10 digits in total and start with 07
- get_possible_nrs(n) accepts a number string n where one digit is missing
- n may be assumed to start with 07 and then contain 7 further digits (in total 9, i.e. one missing digit).
- get_possible_nrs(n) returns a list of whatsapp number strings that might belong to juliet.
- A number that may belong to juliet contains exactly one digit more than n (10 digits).
- The single missing digit may be assumed to be at any index after the starting 07 within n.

Make sure your returned list does not contain duplicates.
wa_nrs is a list of numbers that are registered with Whatsapp.
Compare your generated numbers with the numbers in wa_nrs to return only those from your function which exist in Whatsapp.

Hints
visualize where/at what indices a single digit could be inserted in a given test number
Think of which python constructs you need to populate a list and check for list inclusion
'''
wa_nrs = ["0781111119", "0792653913", "0797763139", "0792793193", "0781139022", "0764320165"]


def get_possible_nrs(n):
    n = ''.join(n.split(' '))
    phone_num = ''
    possible_nrs_for_juliet = []

    # append one digit at every location in the number
    for guess_idx in range(2, len(n)+1):
        for guess_nr in range(10):
            phone_num = n[:guess_idx] + str(guess_nr) + n[guess_idx:]

            # check whether number is in our list
            if phone_num in wa_nrs and not phone_num in possible_nrs_for_juliet:
                possible_nrs_for_juliet.append(phone_num)
        
    return possible_nrs_for_juliet
    

# For this particular number, the function should find the
# last element in wa_nrs
print(get_possible_nrs("076432165"))