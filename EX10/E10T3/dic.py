tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel) #{'jack': 4098, 'sape': 4139, 'guido': 4127}
print(tel['jack'])
#4098
del tel['sape']
print(tel)