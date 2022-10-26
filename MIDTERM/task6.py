'''
Implement a function sum_of_multiplications that 
takes a list of tuples as a parameter. 
Each tuple contains two integers or floats. 
For each tuple, the function should multiply the two values 
and finally it should return the sum of these multiplications.
'''
# sum_of_multiplications([(1, 2), (5, 10)]) should return 52
# because (1 * 2 + 5 * 10) is 52

# Each tuple contains two integers or floats. 
def sum_of_multiplications(l):
    total = 0
    for v1,v2 in l:
        total += v1*v2        
    return total

print(sum_of_multiplications([(1, 2), (5, 10)]))
print(sum_of_multiplications([(1, 2), (3,4), (5,6), (7,8)]))