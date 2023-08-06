from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer


porter = PorterStemmer()
lancaster = LancasterStemmer()
snowball = SnowballStemmer('english')

class PorterStemming():
    def __init__(self, word):
        self.word = word
    
    def reduce(self):
        stemmed = porter.stem(self.word)
        return stemmed

class LancasterStemming():
    def __init__(self, word):
        self.word = word
    
    def reduce(self):
        stemmed = lancaster.stem(self.word)
        return stemmed

class SnowballStemming():
    def __init__(self, word):
        self.word = word
    
    def reduce(self):
        stemmed = snowball.stem(self.word)
        return stemmed


    