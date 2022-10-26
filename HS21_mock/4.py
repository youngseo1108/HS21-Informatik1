'''
Implement a function find_both_ways, which takes two non-empty strings as parameters: text and word. 
The function should determine if the string word appears in the string text, read either normally or backwards, 
while ignoring the casing (see assertions in the template).

If word appears in text from left to right (i.e. read normally), the function should return the tuple (True, 1). 
If word appears in text from right to left (i.e. read in reverse), the function should return the tuple (True, -1). 
If word does not appear, (False, 0) should be returned.

You can assume that the function is only called with valid parameters.
'''
def find_both_ways(text, word):
    text = text.lower()
    word = word.lower()
    if word in text:
        return (True, 1)
    if word in text[::-1]:
        return (True, -1)
    return (False, 0)

# DO NOT SUBMIT THE LINES BELOW!
assert(find_both_ways("Hello, World!", "lo, wo") == (True, 1))
assert(find_both_ways("Hello, God!", "Dog") == (True, -1))
assert(find_both_ways("Hello, California!", "local") == (False, 0))