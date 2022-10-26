'''
Adjust the WordLogic class to inherit the base functionality 
from GameLogic and to make it instantiable by implementing 
the abstract methods. 

To make the current WordLogic implementation
compatible, you also need to adjust the visibilities of 
the existing methods.
'''
from random import choice, shuffle
from game_logic import GameLogic

# This is the current version of WordLogic that needs to be adapted
class WordLogic(GameLogic):

    def _word_selection(self):
        words = self.__find_words_with_right_size()
        shuffle(words)
        return words[0:self.num_words]

    def __find_words_with_right_size(self):
        with open("resource/words.txt") as f:
            word_list = f.read().splitlines()
        return [word.upper() for word in word_list if len(word) is self.len_words]

    def _generate_feedback(self, guess):
        matching = 0
        for i in range(self.len_words):
            if guess[i] == self.password[i]: matching += 1
        self.num_attempts = self.num_attempts - 1
        return "%d/%d correct" % (matching, self.len_words)