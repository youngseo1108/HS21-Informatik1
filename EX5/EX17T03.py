'''
Your task is to write an algorithm that takes a list of strings as input and returns a dictionary, 
containing an index of the words to the matching strings.
- In the dictionary, each key will be a word k, 
- while the value will be a list of indices of the input strings where the word k appears.
- Words should be treated as lowercase only. i.e. Hello and hello should be treated the same.

You can assume that the dataset will contain only lists of strings. You don't need to check the type of the elements in the dataset.
The string data in the dataset will be clean. This means you don't need to worry about cleaning i.e. removing punctation marks or numbers.

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
    for idx, e in enumerate(dataset):
        e = e.lower().split()
        for i in range(len(e)):
            if e[i] not in index_dictionary:
                index_dictionary[e[i]] = [idx]
            else:
                index_dictionary[e[i]].append(idx)
    return index_dictionary

# You can see the output of your function here
print(reverse_index(dataset))
