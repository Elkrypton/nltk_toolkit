try:
    from nltk.stem import WordNetLemmatizer
    from nltk.tokenize import word_tokenize
    from nltk.corpus import stopwords
    import requests
    from bs4 import BeautifulSoup
    from gensim.corpora.dictionary import Dictionary
    from gensim.models.ldamodel import LdaModel
    from typing import Optional
    import time
    import pandas as pd
    import matplotlib.pyplot as plt

except ImportError as err:
    print(":::ERROR IMPORTING MODULE:: {}".format(str(err)))
