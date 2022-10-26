'''
Write a function count_keyword_occurrence that takes two input arguments, 
a string and a list of strings-to-be-searched. 
The function should count how often any of the provided 
strings-to-be-searched occur in the string (do not ignore casing in this task). 
Make sure the function works even if an empty string or empty list is supplied. Hint: You're allowed to use count()
'''
# count_keyword_occurrence(
# "This is a short sentence which serves as an example.",
# ["is", "short"]
# )
# should return 3 because "is" occurs twice and "short" occurs once.
def count_keyword_occurrence(string, strings_to_be_searched):
    total = 0
    for e in strings_to_be_searched:
        total += string.count(e)
    return total

print(count_keyword_occurrence("This is a short sentence which serves as an example.", ["is", "short"]))
print(count_keyword_occurrence('',[]))