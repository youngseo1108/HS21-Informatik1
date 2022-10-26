'''
# TASK 3. REVERSE INDEXING
reverse indexing: inverts keys and values, keys become values and values become keys. 

Your task is to write an algorithm that 
- takes a list of strings as input and returns a dictionary, containing an index of the words to the matching strings.
- In the dictionary, each key will be a word k, 
- while the value will be a list of indices of the input strings where the word k appears.
- Words: lowercase only. i.e. Hello and hello should be treated the same.
- the dataset will contain only lists of strings. You don't need to check the type of the elements in the dataset.
- The string data in the dataset will be clean. This means you don't need to worry about cleaning i.e. removing punctation marks or numbers.

Example
In the example below, the function determines what the indices of the words in the given dataset are. dataset is the list containing the strings.
The reverse_index function is supposed to create and return the dictionary.

dataset = [
    "Hello world",
    "This is the WORLD",
    "hello again"
 ]
res = reverse_index(dataset)

# This assertion checks if the result equals the expected dictinary
assert(res == {
    'hello': [0, 2],
    'world': [0, 1],
    'this': [1],
    'is': [1],
    'the': [1],
    'again':[2]
  }
'''
from collections import defaultdict

# Dataset contains data that will be reverse indexed
dataset = [
    "Hello world",
    "This is the WORLD",
    "hello again"
 ] 

def reverse_index(dataset):    
    index_dictionary = {}
    lst = []

    # first, collect all the words
    for i in range(len(dataset)):
        lst.append(dataset[i].lower().split())
#    return lst
#print(reverse_index(dataset))

    # then append the information to the dictionary / then count
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] not in index_dictionary:
                index_dictionary[lst[i][j]] = [i]
            else:
                index_dictionary[lst[i][j]].append(i)

    # don't forget to return your resulting dictionary
    return index_dictionary

a = ['Numerical methods', 'Informatik1', 'It is shitty', 'numerical methods homework']

# You can see the output of your function here
print(reverse_index(dataset))
print(reverse_index(a))

#sample = {}
#if 'youngseo' not in sample:
#    sample['youngseo'] = [1]
#print(sample)