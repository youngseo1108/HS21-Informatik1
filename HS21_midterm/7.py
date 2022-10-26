'''
Implement a function can_derive, 
which takes a string s, 
and a dictionary chars where the keys are of type char and the values are of type int. 
The dictionary describes, how many times each character can be used. 
Hence, the function should return a bool, stating whether there are sufficient characters to construct the given string s. 
If yes, the function should return True, False otherwise. 
Consider the assert statements given below as examples for can_derive.
'''
def can_derive(s, chars): # chars = {char:int}
    new_dic = {}
    for c in s:
        if c not in new_dic:
            new_dic[c] = 1
        else:
            new_dic[c] += 1
    
    for k,v in new_dic.items():
        if k not in chars or chars[k] < v:
            return False
    return True

assert(can_derive('', {}))
assert(not can_derive('hello', {}))
assert(can_derive('aabb', {'a': 2, 'b': 2}))
print(can_derive('aabb', {'a': 2, 'b': 2}))
print(can_derive('hello', {}))