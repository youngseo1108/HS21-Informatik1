'''
In this task, you will practice list and dict comprehensions
You can find 6 functions in script.py. The first one has already been implemented as an example. The others are for you to finish. 
The import at the beginning simply provides the word list from resource/words.txt as a list.

As a general rule, all functions must start with a return statement and they must return either a list or a dict comprehension. 
The first function is provided as an example. The only exemption to this rule is alphabet().
'''
import words

def words_with_length(length):
    '''this one just serves as an example'''
    return [word for word in words if len(word) == length]

def words_containing_string(s):
    # return a list of all those words from words which contain the given string s
    return [word for word in words if s in word]
# print(words_containing_string('a'))

def words_starting_with_character(c):
    # return a list of all those words from words which start the given character c.
    return [word for word in words if word[0] == c]
# print(words_starting_with_character('a'))

def alphabet():
    '''you don't have to solve this one using a comprehension.
    return a string containing the 26 lower-case latin characters a through z. 
    You may not use the literal string "abcdefghijklmnopqrstuvwxyz" anywhere in your solution! 
    There are other ways of obtaining the alphabet in python (please refer to the internet search engine of your choice).
    '''
    res = ''
    for i in range(97,123):
        res += chr(i)
    return res
print(alphabet())

def dictionary():
    '''
    return a dictionary where each key-value pair consists of a letter of the alphabet
    and a list of all the words starting with the corresponding character. 
    So for example dictionary()["a"] should contain the list of all words starting with "a".
    You can use both the alphabet() and words_starting_with_character(c) functions to your advantage.
    '''
    return {k: words_starting_with_character(k) for k in alphabet()}
# print(dictionary())

def censored_words(s):
    # receives one string s. return a copy of the words list, 
    # in which all words that contain s should be converted to a string of the same length 
    # that only contains lower-case "x" chars. 
    # For example, calling censored_words("bad") would return a list of all words, 
    # but the words "badly", "badge" and "barbados" would have been changed to 
    # "xxxxx", "xxxxx" and "xxxxxxxx", respectively.
    return ['x'*len(word) if s in word else word for word in words]
#    [f(x) if condition else g(x) for x in sequence]

#print(censored_words('ac'))
#print('ac' in 'eacer')