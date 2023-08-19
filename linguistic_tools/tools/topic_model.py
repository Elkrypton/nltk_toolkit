from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import requests
from bs4 import BeautifulSoup

def __init__(self, urls):
    self.url= url 

def Text(self):

    url = "https://cyberconnector.wordpress.com/2021/12/24/quantified-emotions/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    article = soup.find('article')
    full_text = article.get_text()
    return full_text

def Tokenize():
    
    en_stopwords = stopwords.words('english')
    docs = []
    text = Text()
    lmr = WordNetLemmatizer()
    for w in word_tokenize(text):
        if w.isalpha():
            print("===== BEFORE LEMMATIZATION ==")
            print(w[:100])
            w = lmr.lemmatize(w)
            if w not in en_stopwords:
                docs.append(w)
    
    return docs

def to_dict():
    try:
        from gensim.corpora.dictionary import Dictionary
    except ImportError as err:
        print(":::ERROR IMPORTING MODULE:: {}".format(str(err)))

    article_tokens = Tokenize()
    doc_dict = Dictionary(article_tokens)

