

porter = PorterStemmer()
lancaster = LancasterStemmer()
snowball = SnowballStemmer('english')
lmr = WordNetLemmatizer()


def Lemmatize(word):
    lemma = lmr.lemmaize(word)
    return lemma

def PorterStemming(word):
    stemmed = porter.stem(word)
    return stemmed

def LancasterStemming(word):
    
    stemmed = lancaster.stem(word)
    return stemmed

def SnowballStemming(word):
  
    stemmed = snowball.stem(word)
    return stemmed


