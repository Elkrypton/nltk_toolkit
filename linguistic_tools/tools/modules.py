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
    from nltk.probability import FreqDist
    from nltk.stem.lancaster import LancasterStemmer
    from nltk.stem.porter import PorterStemmer
    from nltk.stem.snowball import SnowballStemmer


except ImportError as err:
    print(":::ERROR IMPORTING MODULE:: {}".format(str(err)))
    print("::: FIX THE PROBLEM EITHER WITH INSTALLING, REINSTALLING OR UPDATING THE MODULE::")
    
