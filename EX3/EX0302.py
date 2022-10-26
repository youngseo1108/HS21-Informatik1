'''
A password should contain a variety of characters to make it 
harder to guess. You are part of a team that develops a new 
application, which requires passwords to satisfy the following 
rules:

1. Has a length of 8-16 chars.
2. Only contains the characters a-z, A-Z, digits, or the special 
chars "+", "-", "*", "/".
3. Must contain at least 2 lower case and 2 upper case characters,
2 digits, and 2 special chars.

Implement a checker that decides whether a given password 
candidate is valid. The password candidate will be given to you 
in a variable pwd.

Write a program that checks whether pwd satisfies all rules. 
The validity of the password should be verified by a function 
called is_valid and your task is to complete the function.

Please make sure that your solution is self-contained within the is_valid function. That is, only change the body of the function, not the code outside the function. Your function is expected to return the validity in a bool value.

While working on this task, these utilities will make your life 
easier:
- Use isupper/islower to decide whether a string is upper case 
or lower case (e.g., "A".isupper() is True).
- Use isdigit to check if it is a number (e.g., "3".isdigit() is 
True).
- Use the in operator to check whether a specific character 
exists in a string (e.g., "a" in "abc" is True).
'''
#pwd = "abc"
pwd = 'aaBB+-12'

def is_valid():
    # You need to change the following part of the function
    # to determine if it is a valid password.
    validity = True

    special_char = '+-*/'
    count_low = 0
    count_up = 0
    count_digit = 0
    count_sp = 0
    
    #2. Only contains the characters a-z, A-Z, digits, or the 
    # special chars "+", "-", "*", "/".
    for c in pwd:
        # 2-1. a-z
        if c.islower():
            count_low += 1
        # 2-2. A-Z
        elif c.isupper():
            count_up += 1
        # 2-3. digits
        elif c.isdigit():
            count_digit += 1
        elif c in special_char:
            count_sp += 1
        else:
            validity = False

    #1. Has a length of 8-16 chars.
    validity = validity and len(pwd) >= 8 and len(pwd) <= 16 and count_low > 1 and count_up > 1 and count_digit > 1 and count_sp > 1
    # You don't need to change the following line.
    return validity

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
print(is_valid())