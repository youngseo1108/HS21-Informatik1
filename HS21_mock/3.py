'''
Implement a function recursive_join, which takes two parameters; a string delim and a non-empty list of strings values. 
The function should join the values in values using delim as the delimiter and return the result.

You can assume that the function is only called with valid parameters.

You shouldn't and cannot use str.join in this task. Your solution must be implemented using recursion.
'''
def recursive_join(delim, values):
    if len(values) == 1:
        return values[0]
    return values[0] + delim + recursive_join(delim, values[1:])

# DO NOT SUBMIT THE LINES BELOW!
assert(recursive_join(" ", ["Hello", "world"]) == "Hello world")
assert(recursive_join("  ", ["a", "b", "c"]) == "a  b  c")
assert(recursive_join("", ["a", "b", "c"]) == "abc")
assert("Your solution must be recursive!")

print(recursive_join(" ", ["Hello", "world"]))
print(recursive_join("  ", ["a", "b", "c"]))
print(recursive_join("", ["a", "b", "c"]))