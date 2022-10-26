num1 = 6
num2 = 6

#Function to check whether two numbers are friendly pairs or not.
def isFriendlyPair():
    lst_num1 = []
    lst_num2 = []
    # The numbers must be valid according to description before determining friendly parity situations. 
    # Return "Invalid" if they are not valid.
    if not str(num1).isnumeric() or not str(num2).isnumeric() or num1 == num2:
        return 'Invalid'
    return 'no_prob'

print(isFriendlyPair())