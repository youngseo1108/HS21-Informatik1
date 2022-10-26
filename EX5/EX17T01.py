'''
Write a function that expects two lists of integers, a and b, as parameters and returns a list. 
- The function should merge the elements of both input lists by index 
and return them as tuples in a new list.  
- If one list is shorter than the other, the last element of the shorter list should be repeated as often as necessary. 
- If one or both lists are empty, the empty list should be returned.

Please consider the following examples:

merge([0, 1, 2], [5, 6, 7]) # should return [(0, 5), (1, 6), (2, 7)]
merge([2, 1, 0], [5, 6])    # should return [(2, 5), (1, 6), (0, 6)]
merge([], [2, 3])           # should return []

You can assume that the parameters are always valid lists and you do not need to provide any kind of input validation.
'''
def merge(a, b):
    mergelist = []
    if len(a) == 0 or len(b) == 0:
        return []

    if len(a) > len(b):
        for i in range(len(b)):
            mergelist.append((a[i], b[i]))
        for j in range(len(b), len(a)):
            mergelist.append((a[j], b[-1]))

    elif len(a) < len(b):
        for i in range(len(a)):
            mergelist.append((a[i], b[i]))
        for j in range(len(a), len(b)):
            mergelist.append((a[-1], b[j]))

    else:
        for i in range(len(a)):
            mergelist.append((a[i], b[i]))

    return mergelist

print(merge([0, 1, 2], [5, 6]))
print(merge([0, 1, 2], [5, 6, 7])) # should return [(0, 5), (1, 6), (2, 7)]
print(merge([2, 1, 0], [5, 6]))    # should return [(2, 5), (1, 6), (0, 6)]
print(merge([], [2, 3]))           # should return []