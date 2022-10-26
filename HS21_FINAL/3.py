'''
Implement a function count_palindromes, 
- which takes a string as parameter sentence. 
- return the number of palindromes in sentence as an integer. 

A palindrome is a word that can be read the same forwards and backwards. 
- A palindrome must be at least 3 characters long. 
- The function should be case-insensitive and ignore special characters in words. 

Consider the assertions given below as examples for using count_palindromes.
'''
def count_palindromes(sentence):
    count = 0
    sentence = sentence.lower().split(" ")

    for e in sentence:
        e = ''.join(c for c in e if c.isalpha())
        if len(e) >= 3 and e == e[::-1]:
            count += 1
    return count

# DO NOT SUBMIT THE LINES BELOW!
assert count_palindromes("Having fun!") == 0
assert count_palindromes("Bob and otto") == 2
assert count_palindromes("Where's Dad?") == 1
assert count_palindromes("Otto is my dad.") == 2
assert count_palindromes("I don't like pop music") == 1

#print(count_palindromes("I don't like pop music"))
