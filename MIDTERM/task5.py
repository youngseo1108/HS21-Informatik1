'''
Write a function list_reversed_filtered which takes two lists, l1 and l2, as input parameters. 
The function should return the reverse of l1, but without any elements which exist in l2.
'''
# list_reversed_filtered([1,2,3,4,5], [1,3]) should return [5,4,2]
def list_reversed_filtered(l1, l2):
    l = []
    for i in range(len(l1)-1, -1, -1):
        if l1[i] not in l2:
            l.append(l1[i])
    return l

print(list_reversed_filtered([1,2,3,4,5], [1,3]))
print(list_reversed_filtered([1,2,3,4,5], [1,2,3]))
print(list_reversed_filtered([1,2,3,4,5], [2,3,5]))
#l = [1,2,3,4,5]
#print(l[::-1])
#print(l[::-2])
#print(l[:-1])

# Method
def list_reversed_filtered(l1, l2):
    res = []
    index = len(l1)-1
    while index >= 0:
        if not l1[index] in l2:
            res.append(l1[index])
        index -= 1
    return res