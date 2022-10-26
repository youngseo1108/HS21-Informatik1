'''
Write a function called is_palindrome that takes a string as a parameter. 
The function should first remove all non-alphabetical characters from the string. 
Then it should check if the given resulting character sequence is a palindrome (ignoring casing). 
A palindrome is something that reads the same forwards and backwards. 
Here are some examples, for which the function should positively detect a palindrome: 
"bob", "UFO-tofu", "Senile felines!", "No lemons, no melon". 
The function should return True when identifying a palindrome, False otherwise.
'''
# is_palindrome("Was it a car or a cat I saw?") should return True
# is_palindrome("Programming is hard.") should return False
def is_palindrome(s):
    # first remove all non-alphabetical characters from the string
    string = ''
    for ch in s:
        if ch.isalpha():
            string += ch.lower()
    return string == reversed(string)

print(is_palindrome("Was it a car or a cat I saw?"))
print(is_palindrome("Programming is hard."))