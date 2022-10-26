'''
Applying nested loops often requires, that the inner loop accesses
the outer loop variable. This exercise leverages the outer loop 
variable as an index for the inner loop's range and thus, 
provides the opportunity to deepen the understanding of nested 
loops. The goal of this task is to build a string that resembles 
a pyramid when printed to the console. The resource folder 
contains examples for pyramids of different heights.

[Specification of the pyramid string]
Given a parameter n for the pyramid height, the string should 
adhere to the following pattern:
- the number of lines in the console output should be 2*n -1.
- the n-th line should be of length n (excl. the new line 
character "\n"), all others should be shorter, decreasing by one 
with each step further away from the n-th line.
- each line should contain numbers starting from 1 to i, where i
denotes the given line number, and where the numbers are 
separated via an asterisk "*"
- h can be assumed non-negative, where height 0 is the empty 
string.

Hints:
- use the range() function and take care of the indices
- use the "\n" newline character at the end of every line
- concatenating numbers and strings requires the str() function
- try to break down the problem into chunks: start by printing 
the first half of the pyramid and getting it to work before 
going on to the reverse part.
'''
h = 10

# build a string 
def build_string_pyramid():
    # You need to change the functionality of this function to
    # create the correct 'encoded' string which will be returned
    # at the end of the function.
    s = ""

    # use nested loops and the range() function
    for i in range (1, h+1):
        s += '1'
        for j in range(2, i+1):
            s += '*' + str(j)
        s += '\n'

    for i in range(h+1, 2, -1):
        s += '1'
        for j in range(2, i-1):
            s += '*' + str(j)
        s += '\n'
    # You don't need to change the following line.
    # It simply returns the string created above.
    return s

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# See the console output and compare it to the image in the task description
print(build_string_pyramid())