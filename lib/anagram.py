# your code goes here!class 
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, words):
        anagrams = []
        for candidate in words:
            if self.is_anagram(candidate):
                anagrams.append(candidate)
        return anagrams

    def is_anagram(self, candidate):
        candidate_lower = candidate.lower()
        if candidate_lower == self.word:
            return False
        return sorted(candidate_lower) == sorted(self.word)
