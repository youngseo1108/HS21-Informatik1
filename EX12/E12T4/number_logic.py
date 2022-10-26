'''
Finally, create the new class NumberLogic that extends GameLogic and works as follows:

- On initialization, it generates string sequences of numbers (e.g., for len_words=4 examples would be "1234", "5291", "5930", ...). 
These sequences may only contain each specific number exactly once. 
As a result, "0000" would be an invalid number, because 0 is contained multiple times.
- The same rules of WordLogic apply as well. The logic should generate num_words candidate sequences that all have a length of len_words digits. 
Both are stored as public variables in the base class and can therefore be directly accessed.
- One of the generated sequences is randomly picked as the secret and the goal is to guess the secret.
- The player can add guesses by calling the GameLogic.check function. 
As long as attempts are left, the system will return feedback through the NumberLogic._generate_feedback method 
that describes how close the guess is to the secret.
- In contrast to WordGame, the numbers are NOT compared index-by-index, the system will only say how many numbers from the guess 
also appear in the secret. For example, if the secret is "1063", a guess "1234" would get the feedback "2/4 correct", 
because both contain the numbers 1 and 3. While a guess "3601" would get the feedback "4/4 correct", 
it is still not the accepted solution due to the wrong number order.
- NumberLogic should override the check method and reject guesses that contain repeated numbers or have the wrong length by raising a Warning. 
If a guess is valid, the call should be delegated to the super class.

Note: The list returned by word_selection may not contain any duplicates
Note: Let both NumberLogic and WordLogic inherit from GameLogic. 
Both subclasses must not specify their own constructors: it must only exist in the abstract GameLogic class. 
Likewise, WordLogic should not implement check, and NumberLogic's override of check must only extend the check function to reject guesses 
(calling check in the super class eventually), not duplicate it entirely.
'''
from game_logic import GameLogic
import random

class NumberLogic(GameLogic):

    def _word_selection(self):
        # On initialization, it generates string sequences of numbers 
        # (e.g., for len_words=4 examples would be "1234", "5291", "5930", ...). 
        # These sequences may only contain each specific number exactly once.
        num = [0,1,2,3,4,5,6,7,8,9]
        seq_num = ''
        n = self.len_words
        while n > 0:
            if str(random.choice(num)) not in seq_num:
                seq_num += str(random.choice(num))
                n -= 1
        return seq_num

    def _generate_feedback(self, guess):
        pass


    def check(self, guess):
        for i in range(0,len(guess)-1):
            for j in range(1,len(guess)):
                if guess[i] == guess[j]:
                    raise Warning('Duplicate Numbers.')           
        super().check(guess)

#        if self.num_attempts == 0:
#            raise Warning("No attempts left")
#        if len(guess) != self.len_words:
#            return False, ["Wrong length"]
#        if guess == self.password:
#            return True, ["Access granted!"]
#        else:
#            return False, [
#                self.generate_feedback(guess),
#                "Access denied!"
#            ]
