'''
You are part of a team that develops a new application, which requires passwords to satisfy the following rules:
- Has a length of 8-16 chars.
- Only contains the characters a-z, A-Z, digits, or the special chars "+", "-", "*", "/".
- Must contain at least 2 lower case and 2 upper case characters, 2 digits, and 2 special chars.
- Implement a checker that decides whether a given password candidate is valid. 
The password candidate will be given to you in a variable pwd.

Write a program that checks whether pwd satisfies all rules. 
The validity of the password should be verified by a function called is_valid and your task is to complete the function.

While working on this task, these utilities will make your life easier:
- Use isupper/islower to decide whether a string is upper case or lower case (e.g., "A".isupper() is True).
- Use isdigit to check if it is a number (e.g., "3".isdigit() is True).
- Use the in operator to check whether a specific character exists in a string (e.g., "a" in "abc" is True).
'''
#pwd = 'aaAA00++#'
pwd = 'aaAA00++'

def is_valid():
#- Implement a checker that decides whether a given password candidate is valid. 
#The password candidate will be given to you in a variable pwd.

    validity = True
    chars = '+-*/'
    lower = 0
    upper = 0
    digit = 0
    special_char = 0

    # Must contain at least 2 lower case and 2 upper case characters, 2 digits, and 2 special chars.
    for c in pwd:
        # Only contains the characters a-z, A-Z, digits, or the special chars "+", "-", "*", "/".
        if c.islower(): lower += 1
        elif c.isupper(): upper += 1
        elif c.isdigit(): digit += 1
        elif c in chars: special_char += 1
        else: 
            validity = False
        # Has a length of 8-16 chars.        
    
    validity = validity and len(pwd) >= 8 and len(pwd) <= 16 and lower > 1 and upper > 1 and digit > 1 and special_char > 1
    # You don't need to change the following line.
    return validity

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
print(is_valid())