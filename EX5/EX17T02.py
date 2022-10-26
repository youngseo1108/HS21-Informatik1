'''
In this task, you will write a function analyze that scans a list of social media posts for such hashtags. 
- receive a list of posts as a parameter posts. 
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

A Hashtag is defined as a '#' followed by any combinations of letters (lower/upper) and numbers. 
- only the basic characters available in ASCII can be used in a hashtag (i.e., a-z, A-Z, 0-9). 
- Every other character (e.g., space or '.') ends the current hashtag. 
- Hashtags need to start with a letter (i.e. not number. e.g. #1 is not a valid hashtag) and cannot be empty.

Note: For this task, hashtags are case-sensitive. #ZURICH should be counted as a different hashtag than #zurich.
'''
#!/usr/bin/env python3

def analyze(posts):
    tags = {}

    for post in posts:
        curHashtag = None
        for c in post:
            is_allowed_char = c.isalnum()

            if curHashtag != None and not is_allowed_char:
                if len(curHashtag) > 0 and not curHashtag[0].isdigit():
                    if curHashtag in tags.keys():
                        tags[curHashtag] += 1
                    else:
                        tags[curHashtag] = 1
                curHashtag = None

            if c == "#":
                curHashtag = ""
                continue

            if c.isalnum() and curHashtag != None:
                curHashtag += c

        if curHashtag != None:
            if len(curHashtag) > 0 and not curHashtag[0].isdigit():
                if curHashtag in tags.keys():
                    tags[curHashtag] += 1
                else:
                    tags[curHashtag] = 1

    return tags

posts = [
    "hi #weekend",
    "good morning #zurich #limmat",
    "spend my #weekend in #zurich",
    "#zurich <3"]
print(analyze(posts))