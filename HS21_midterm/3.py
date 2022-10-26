'''
Implement a function , which takes two lists of items a, and b, 
and returns True if all of the elements found in b can also be found in a. 
The function returns False otherwise. 
Furthermore, if b is an empty list, then the function always returns True regardless of the content of a. 
You can assume the values for a and b are always non-null lists. Consider the assert statements given below as examples for is_sub_collection.
'''
def is_sub_collection(a, b):
    for e in b:
        if e not in a:
            return False
    return True

assert(is_sub_collection([], []))
assert(not is_sub_collection([], [True]))
assert(is_sub_collection([1, 2, 3, None], [None]))

print(is_sub_collection([1, 2, 3, None], [None]))