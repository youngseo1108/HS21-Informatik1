'''
O. friendly number: a natural number that shares a certain 
characteristic called abundancy with one or more other numbers. 

O. Abundancy: the ratio between the sum of divisors of the number
and the number itself. Two different numbers with the same
abundancy form a friendly pair.
- abundancy of n: σ(n) / n, 
- σ denotes the sum of divisors function. 
- n: a friendly number if there exists m ≠ n
where σ(m) / m = σ(n) / n.
- σ(n): the sum of divisors

eg) σ(6) = 1+2+3+6 = 12
abundancy of 6 (σ(n) / n): σ(6) / 6 = 12 / 6 = 2
abundancy of 28: σ(28) / 28 = (1+2+4+7+14+28) / 28 = 2
Since abundancies of 6 and 28 are both 2 -> friendly pair

Your task:
implement an algorithm in the function isFriendlyPair which 
checks whether two numbers are a friendly pair or not.

Hint 1: Try to understand the problem first. Use pen and paper to
break down the problem.
Hint 2: Please make sure the function returns the correct types.
'''
#You are completely free to change this variables to check your algorithm.
num1 = -6
num2 = 28

#Function to check whether two numbers are friendly pairs or not.
def isFriendlyPair():
    lst_num1 = []
    lst_num2 = []
    # The numbers must be valid according to description before determining friendly parity situations. 
    # Return "Invalid" if they are not valid.
    if not str(num1).isnumeric() or not str(num2).isnumeric() or num1 == num2:
        return 'Invalid'

    # 1-1. find divisors of num1
    for i in range(1, num1 + 1):
        if num1 % i == 0:
            lst_num1.append(i)

    # 1-2. find divisors of num2
    for i in range(1, num2+1):
        if num2 % i == 0:
            lst_num2.append(i)

    # 2-1. caculate abundancy of num1
    sig_num1 = 0
    for n1 in lst_num1:
        sig_num1 += n1
    # 2-2. calculate abundancy of num2
    sig_num2 = 0
    for n2 in lst_num2:
        sig_num2 += n2

    if (sig_num1 / num1) != (sig_num2 / num2):
        return False
    # If num1 & num2 are friendly pairs return True, else, False. 
    return True

#This line prints your method's return so that you can check your output.
print(isFriendlyPair())