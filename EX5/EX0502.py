'''
TASK 2. HASHTAG ANALYSIS
In this task, you will write a function analyze that scans a list of social media posts for such hashtags. 
The function will receive a list of posts as a parameter posts. 
Your task is 
- to analyze the strings, identify the hashtags, and count them. 
- The result should be a dictionary, where the keys are hashtags and the values are their respective count.

For example, consider the following list of posts:
[
    "hi #weekend",
    "good morning #zurich #limmat",
    "spend my #weekend in #zurich",
    "#zurich <3"
]

After analyzing this list, your function should return:
{'weekend': 2, 'zurich': 3, 'limmat': 1}

Hashtag: '#' followed by any combinations of letters (lower/upper) and numbers. 
assume that only the basic characters that are available in ASCII can be used in a hashtag (i.e., a-z, A-Z, 0-9). 
Every other character (e.g., space or '.') ends the current hashtag. 
Hashtags need to start with a letter (i.e. not number. e.g. #1 is not a valid hashtag) and cannot be empty.

You can assume that the parameter is always a valid list of strings and you do not need to provide any kind of input validation.

Note: For this task, hashtags are case-sensitive. #ZURICH should be counted as a different hashtag than #zurich.
Note: It is highly recommended that you update the public test to include more border cases, such as invalid hashtags 
(e.g. empty or starting with a number) to ensure that your solution also works in those cases!
'''
from collections import Counter
import re

def analyze(posts):
    hash_counts = Counter(re.findall(r'#(\w*[a-zA-Z]+\w*)', ' '.join(posts), re.I))
    return dict(hash_counts)

posts = [
    "hi #weekend",
    "good morning #zurich #limmat",
    "spend my #weekend in #zurich",
    "#zurich <3",
    "#Zurich", "#012", "# zURICH"]
print(analyze(posts))
