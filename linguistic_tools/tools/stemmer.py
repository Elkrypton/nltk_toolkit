from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer


porter = PorterStemmer()
lancaster = LancasterStemmer()
snowball = SnowballStemmer('english')


def PorterStemming(word):
    stemmed = porter.stem(word)
    return stemmed

def LancasterStemming(word):
    
    stemmed = lancaster.stem(word)
    return stemmed

def SnowballStemming(word):
  
    stemmed = snowball.stem(word)
    return stemmed


