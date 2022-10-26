'''
In number theory, a friendly number is a natural number that shares a certain characteristic called abundancy with one or more other numbers. 
Abundancy is the ratio between the sum of divisors of the number and the number itself. 
Two different numbers with the same abundancy form a friendly pair.

The abundancy of n is the rational number σ(n) / n, in which σ denotes the sum of divisors function. 
A number n is a friendly number if there exists m ≠ n where σ(m) / m = σ(n) / n.

For example 6 is a friendly number because abundancy of 6 and 28 are same : 2. Thus 6 and 28 are friendly pair

The divisors of 6 are 1, 2, 3, 6. σ(n) is calculated as the sum of divisors.
So in this case σ(6) = 1+2+3+6 = 12. We found σ(6) = 12. Now we need to calculate the abundancy of 6.
The abundancy is σ(n) / n . So in this case: σ(6) / 6 = 12 / 6 = 2
So the abundancy of 6 is 2.
Now we calculate the abundancy of 28: σ(28) / 28 = (1+2+4+7+14+28) / 28 = 2.
Since abundancies of 6 and 28 are both 2 we call (6, 28) a friendly pair.
Your task is to implement an algorithm in the function isFriendlyPair which checks whether two numbers are a friendly pair or not.

Hint 1: Try to understand the problem first. Use pen and paper to break down the problem. Coding will be a lot easier if you are able to solve the problem on paper first and determine the steps on paper.
Hint 2: Please make sure the function returns the correct types.
'''
#You are completely free to change this variables to check your algorithm.
num1 = 6 
num2 = 28

#Function to check whether two numbers are friendly pairs or not.
def isFriendlyPair():
    # The numbers must be valid according to description before determining friendly parity situations. 
    # Return "Invalid" if they are not valid.
    if num1 == num2 or type(num1) != int or type(num2) != int:
        return 'Invalid'

    n1 = []
    n2 = []
    for n in range(1, num1+1):
        if num1 % n == 0:
            n1.append(n)
    
    for n in range(1, num2+1):
        if num2 % n == 0:
            n2.append(n)

    sig1 = sum(n1) / num1
    sig2 = sum(n2) / num2
    
    return sig1 == sig2

#This line prints your method's return so that you can check your output.
print(isFriendlyPair())