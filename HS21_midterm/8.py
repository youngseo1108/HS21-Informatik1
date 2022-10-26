x = 0
a = 1
b = 0
c = []
def func(a):
   if a < 0:
       b = -1
   elif a == 0:
       c.append(-2)
   else:
       a = func(a - 1) - 3
   return a
#func(x)
print(func(x))
print(c)