try:
    from nltk.stem import WordNetLemmatizer
    from nltk.tokenize import word_tokenize
    from nltk.corpus import stopwords
    import requests
    from bs4 import BeautifulSoup
    from gensim.corpora.dictionary import Dictionary
    from typing import Optional
    import time
except ImportError as err:
    print(":::ERROR IMPORTING MODULE:: {}".format(str(err)))


def fetch_article(url: str) -> str:
    """
    Fetches the article from the url and returns it as a string
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content)
    article = soup.find("div", class_ = "card-body-big")
    full_text = article.get_text()
    return full_text

def tokenize_article(article: str, extra_stops: Optional[list]: None ) -> list[str]:
    """
    Tokenizes the article into a list of words
    """
    en_stopwords = stopwords.words('english')
    if extra_stops:
        en_stopwords += extra_stops

    article_stopwords = set(en_stopwords)
    lmr = WordNetLemmatizer()
    #tokenize the text
    article_tokens = []
    for word in word_tokenize(article):
        if word.isalpha():
            word = lmr.lemmatize(word.lower())
            if word not in article_stopwords:
                article_tokens.append(word)
    return article_tokens




