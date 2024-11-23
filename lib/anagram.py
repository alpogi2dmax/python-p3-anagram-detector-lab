# your code goes here!
class Anagram:
    
    def __init__(self, word):
        self.word = word

    def match(self, word_array):
        match_array = []
        for x in word_array:
            if sorted(self.word) == sorted(x):
                match_array.append(x)
        return match_array