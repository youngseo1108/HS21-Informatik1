'''
Implement a function contains_duplicates 
which takes a list of arbitrary elements l as the only parameter. 
The function should return True if the list contains two or more identical items, 
False otherwise. 
You can assume that the function is only called with valid parameters.
'''
def contains_duplicates(l):
    for i in range(len(l)-1):
        for j in range(i+1,len(l)):
            if l[i] == l[j]:
                return True
    return False

assert(not contains_duplicates([1,2,3]))
assert(contains_duplicates([1,2,2]))
assert(contains_duplicates(["a","b","a"]))
assert(contains_duplicates(["a","a","a"])) # fails!

# Here are three more sensible solutions that actually work correctly, just FYI:

def contains_duplicates(l):
    seen = []
    for elem in l:
        if elem in seen: return True
        seen.append(elem)
    return False

def contains_duplicates(l):
    for elem in l:
        if l.count(elem) > 1: return True
    return False

def contains_duplicates(l):
    return not len(l) == len(set(l))