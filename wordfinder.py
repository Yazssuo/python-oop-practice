"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    """Makes a list of words from dictionary and create method for returning random word
    
    >>> wf = WordFinder("words.txt")
    3 words read

    >>> wf.random() in ["william", "taylor", "hanna"]
    True

    >>> wf.random() in ["william", "taylor", "hanna"]
    True

    >>> wf.random() in ["william", "taylor", "hanna"]
    True
    
    """


    def __init__(self, filename):
        dictionary = open(filename)
        self.words = self.getWords(dictionary)
        print(f"{len(self.words)} words read")

    def getWords(self, file):
        """Get words from dictionary"""
        return [word.strip() for word in file]
    
    def random(self):
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    """Word Finder but with additional requirements
    
    >>> wf = SpecialWordFinder("words2.txt")
    4 words read

    >>> wf.random() in ["Grapes", "Oranges", "Tomatoes", "Cabbage"]
    True

    >>> wf.random() in ["Grapes", "Oranges", "Tomatoes", "Cabbage"]
    True

    >>> wf.random() in ["Grapes", "Oranges", "Tomatoes", "Cabbage"]
    True

    """
    def getWords(self, file):
        """Get words from dictionary and ignore whitespace and #"""
        return [word.strip() for word in file if word.strip() and not word.startswith("#")]