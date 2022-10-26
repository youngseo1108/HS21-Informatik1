'''
Programming
Implement a recursive function recursive_reverse 
that takes a string parameter 
and returns the reverse of the same string. 
In this task, you may not make any function calls except recrusive calls to the solution function.
'''
# recursive_reverse("hello") should return "olleh"
def recursive_reverse(s):
    if len(s) == 0:
        return s
    else:
        return recursive_reverse(s[1:]) + s[0]

print(recursive_reverse('hello'))