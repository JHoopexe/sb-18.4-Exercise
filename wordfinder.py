"""Word Finder: finds random words from a dictionary."""
from random import choice

class WordFinder:
    def __init__(self,file_name):
        open_file = open(file_name,"r")
        self.words = []
        for word in open_file:
            self.words.append(word.rstrip())
        print(f"{len(self.words)} words read")
        close_file = open_file.close()
        
    def random(self):
        return choice(self.words)

class SpecialWordFinder(WordFinder):
    def __init__(self,file_name):
        super().__init__(file_name)
        self.words2 = []
        for line in self.words:
            if line.strip() and not line.startswith("#"):
                self.words2.append(line)

    def random2(self):
        return choice(self.words2)
