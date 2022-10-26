#!/usr/bin/env python3
'''
First of all, create an abstract GameLogic class. 
Remember that abstract classes need to extend ABC and 
annotate all their abstract methods with @abstractmethod. 
Move the current constructor (__init__) and the check method 
from WordLogic to GameLogic. 
The content is not specific to WordLogic and can be re-used. 
GameLogic should introduce two abstract methods 
_word_selection and _generate_feedback, 
which should have a protected visibility, 
the former should be used in the constructor, 
the latter in the check method.
'''
# TODO: Implement Me!
from abc import ABC, abstractmethod
from random import choice

class GameLogic(ABC):

    def __init__(self, num_words, len_words, num_attempts):
        self.num_words = num_words
        self.len_words = len_words
        self.num_attempts = num_attempts
        self.words = self._word_selection()
        self.password = choice(self.words)

    @abstractmethod
    def _word_selection(self):
        pass

    @abstractmethod
    def _generate_feedback(self, guess):
        pass

    def check(self, guess):
        if self.num_attempts == 0:
            raise Warning("No attempts left")
        if len(guess) != self.len_words:
            return False, ["Wrong length"]
        if guess == self.password:
            return True, ["Access granted!"]
        else:
            return False, [
                self.generate_feedback(guess),
                "Access denied!"
            ]
