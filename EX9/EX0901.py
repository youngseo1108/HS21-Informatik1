'''
# TASK 1. Profanity Filter
In this task, you will implement a ProfanityFilter class 
that can be used to redact swear words in messages. Please see the following example that illustrates all relevant functions.

f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
offensive_msg = "abc defghi mastard jklmno"
clean_msg = f.filter(offensive_msg)
print(clean_msg) # abc defghi ?#$?#$? jklmno

The filter gets initialized with a list of offensive keywords and a replacement template. 
Every occurence of any of these words should be replaced with a string that is generated from the template. 
- If the word size is shorter than the template, a substring should be used that starts from the beginning, 
- for longer sizes, the template should be repeated as often as necessary. 
- case-insensitive, so regardless of how the keywords are defined or in which form they appear in the text, they should get replaced.

The keywords can be provided in any order and might contain each other as subwords. The profanity filter has to properly replace every word though, so make sure to sort the list of offensive words by size and replace larger words first to avoid a subword-only replacement. Make sure that you also replace offensive words that only occur as a subword (e.g. "fishotter" should become "fi?#$?ter").

You can implement the class the way you like. 
Apart from the signature of constructor and filter no requirements will be enforced. 
We encourage you to use utility functions in the class, but this is up to you. 
You could, for example, create a private function __clean that generates an escaped sequence for a provided word of an arbitrary length 
(e.g., in the example clean("batch") == "?#$?#").

Note: You can use the function str.replace to make the replacement easier and sorted/reversed to help you with the sorting.
'''
# trial 1
'''
class ProfanityFilter:

    def __init__(self, keywords, template):
        self.__keywords = keywords
        self.__template = template

    def filter(self, msg):
        # sort the keywords by length
        self.__keywords = sorted(self.__keywords, key=len, reverse=True)
        # replace largerwords first to avoid subword only replacement
        for i in range(len(self.__keywords)):
            num_of_repeat = len(self.__keywords[i]) // len(self.__template) + 1
            new_temp = self.__template * num_of_repeat
            msg = msg.lower().replace(self.__keywords[i].lower(), new_temp[:len(self.__keywords[i])])
        return msg

    def __str__(self) -> str:
        return f'{self.filter}'
'''

class ProfanityFilter:

    def __init__(self, keywords, template):
        self.__keywords = []
        for k in keywords:
            self.__keywords.append(k.lower())
        self.__keywords = sorted(self.__keywords, key=len, reverse = True)
        self.__template = template

    def filter(self, msg):
        msg_ci = msg.lower()
        for k in self.__keywords:
            while k in msg_ci:
                idx = msg_ci.find(k)
                msg = self.__replace(msg, idx, k)
                msg_ci = self.__replace(msg_ci, idx, k)
        return msg

    def __replace(self, ch, idx, word):
        res = ''
        for i in range(len(word)):
            t_idx = i % len(self.__template)
            res += self.__template[t_idx]
        return ch[:idx] + res + ch[idx+len(res):]

if __name__ == '__main__':
    f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
    offensive_msg = "abc defghi mastard jklmno"
    a = 'duck shot BaTch Kiss me more'
    clean_msg = f.filter(offensive_msg)
    print(clean_msg)  # abc defghi ?#$?#$? jklmno
    print(f.filter(a))
