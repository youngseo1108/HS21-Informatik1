print("int(1)" + "2")

'''
Implement a function where_is_waldo, 
which takes a list of strings as a parameter names 
and returns the index of the string "Waldo" within names. 
If "Waldo" appears more than once, the first index should be returned. If "Waldo" is not in names, the function should return None.
Consider the assertions as examples for how where_is_waldo can be used.
'''

def where_is_waldo(names):
    for i in range(len(names)):
        if names[i] == 'Waldo':
            return i
    return None


print(where_is_waldo(["Peter", "Waldo", "John"]))
print(where_is_waldo(["Peter", "Willy", "John"]))
print(where_is_waldo([]))
print(where_is_waldo(["Peter", "Youngseo", "Alex", 'Waldo', "Waldo", "John"]))
#assert(where_is_waldo(["Peter", "Waldo", "John"]) == 1)
#assert(where_is_waldo(["Peter", "Willy", "John"]) == None)
#assert(where_is_waldo([]) == None)
#assert(where_is_waldo(["Peter", "Youngseo", "Alex", 'Waldo', "Waldo", "John"]) == 3)