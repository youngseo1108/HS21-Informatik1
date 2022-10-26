a = (1, [])

def func(a, lst):
   a[0] = lst + lst
   a += [(3, 4), lst]
   return a

print(func(a,[]))

'''
EN: Function 'func' when invoked as is on any value of 'str_freq', can never modify the value of 'str_freq' (declared in line 1).
EN: Function 'func' contains a bug guaranteed to lead to a crash for any instance of 'str_list'.
EN: Function 'func' contains a bug guaranteed to lead to a crash for any non empty instance of 'str_list'.
EN: Every time function 'func' is invoked the value of 'str_freq' (declared in line 1) is overwritten.
'''