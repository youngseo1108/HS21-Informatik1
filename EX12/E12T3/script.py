'''
1. Implement the method WordLogic.is_similar(self, a, b, threshold) which computes the similarity between a and b. 
It shall return True if the ratio is (strictly) higher than threshold or False otherwise. 
Use SequenceMatcher.ratio to compute the similarity.

2. Adjust the function word_selection to implement the following strategy for choosing a total of num_words words 
from the shuffled list of fixed-length words.
2.1 Pick one-third of num_words at random. Use floor to handle cases in which num_words is not dividable by 3.
2.2. For the remaining words:
- Randomly pick one of the already selected words by using choice.
- Randomly pick a word from the remaining word pool. Add it to the list of selected words if compute_similarity confirms more than 40% similarity.
- Repeat until enough sufficiently similar words have been found. You can assume that it is always possible to find such a word and you do not need to prevent endless loops.

Note: Instead of repeatedly performing a random selection, you can also shuffle a list once 
and then just iterate over all elements or slice the list to get a random subset.

Note: The list returned by word_selection may not contain any duplicates

Note: Make sure that your implementation is fast, especially the word selection. 
If the execution takes longer than 3s, it will be terminated and you will see a crash report in the solution hint.
'''
import random
from difflib import SequenceMatcher

class WordLogic(object):

    def __init__(self, num_words, len_words):
        self.num_words = num_words
        self.len_words = len_words

    def find_words_with_right_size(self):
        with open("words.txt") as f:
            word_list = f.read().splitlines()
        return [word.upper() for word in word_list if len(word) is self.len_words]

    def word_selection(self):
        words = self.find_words_with_right_size()
        random.shuffle(words)
        # 2.1 Pick one-third of num_words at random. Use floor to handle cases in which num_words is not dividable by 3.
        n = len(words)//3
        words_pick = words[0:n]
        # 2.2. For the remaining words:
        words_remaining = []
        for word in words:
            if word not in words_pick:
                words_remaining.append(word)
        def compute_similarity(a, b):
            return SequenceMatcher(None, a, b).ratio()
        while True:
            # - Randomly pick one of the already selected words by using choice.
            a = random.choice(words_pick)
            # - Randomly pick a word from the remaining word pool.
            b = random.choice(words_remaining)
            # Add it to the list of selected words if compute_similarity confirms more than 40% similarity.
            if compute_similarity(a, b) > 0.4:
                words_pick.append(b)
                words_remaining.remove(b)
            if len(words_remaining) == 0:
                break
            # - Repeat until enough sufficiently similar words have been found.
            # You can assume that it is always possible to find such a word and you do not need to prevent endless loops.
        return words_pick[0:self.num_words]
    
    def is_similar(self, a, b, threshold):
        # computes the similarity between a and b. 
        # It shall return True if the ratio is (strictly) higher than threshold or False otherwise. 
        # Use SequenceMatcher.ratio to compute the similarity.
        if SequenceMatcher(None, a, b).ratio() > threshold:
            return True
        return False


# print(SequenceMatcher(None, 'Youngseo', 'youngseo').ratio()) # 0.875
w = WordLogic(10, 7) # num_words, len_words
words = w.word_selection()
assert len(words) == w.num_words