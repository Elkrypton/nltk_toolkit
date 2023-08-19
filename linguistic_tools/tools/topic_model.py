
from modules import *

def fetch_article(url: str) -> str:
    """
    Fetches the article from the url and returns it as a string
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    full_text = soup.get_text()
    return full_text

def tokenize_article(article: str, extra_stops: Optional[list] =  None ) -> list[str]:
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

urls = [
    'https://thecodinginterface.com/blog/spam-ham-ml-scikit-learn/',
    'https://thecodinginterface.com/blog/opencv-Mat-from-array-and-vector/',
    'https://thecodinginterface.com/blog/sql-window-functions/',
    'https://thecodinginterface.com/blog/bridging-nodejs-and-python-with-pynode/',
    'https://thecodinginterface.com/blog/django-auth-part1/',
    'https://thecodinginterface.com/blog/django-auth-part4/',
    'https://thecodinginterface.com/blog/intro-to-java-for-devs/',
    'https://thecodinginterface.com/blog/text-analytics-app-with-flask-and-textblob/',
    'https://thecodinginterface.com/blog/aws-s3-python-boto3/',
    'https://thecodinginterface.com/blog/intro-to-pyspark/',
    'https://thecodinginterface.com/blog/java-web-scraping-app-with-jsoup-and-javafx/',
    'https://thecodinginterface.com/blog/javafx-alerts-and-dialogs/',
    'https://thecodinginterface.com/blog/intro-to-pyflink/',
    'https://thecodinginterface.com/blog/opencv-cpp-vscode/'
]

docs = []

for url in urls:
    article_txt = fetch_article(url)
    time.sleep(2)
    article_tokens = tokenize_article(article_txt, extra_stops=['div', 'java'])
    docs.append(article_tokens)

corpus_dict = Dictionary(docs)




print("Count of terms before filteration : {}".format(len(corpus_dict)))


corpus_dict.filter_extremes(no_below=1, no_above=0.5)

print("Count of terms after filteration : {}".format(len(corpus_dict)))

corpus = [corpus_dict.doc2bow(doc)for doc in docs]

n_topics = 16
lda = LdaModel(corpus, num_topics=n_topics, random_state=23, id2word=corpus_dict)
topic_mat  = lda.get_topics()
ids, cols = zip(*lda.id2word.items())
df = pd.DataFrame(topic_mat, columns=cols)
df.iloc[:, ::300]


topics = lda.show_topics(num_topics=n_topics, num_words=5, formatted=False)
topics = sorted(topics, key=lambda x: int(x[0]))

rows = 4
cols = 4

fig, axs = plt.subplots(nrows=rows, ncols=cols, sharex=True, figsize=(12,8))

for topic_id, word_props in topics:
    row = topic_id // rows
    col = topic_id - (row* cols)
    ax  = axs[row, col]
    words, probs= zip(*word_props)
    ax.barh(words, probs)
    ax.invert_yaxis()
    ax.set_title('Topic {}'.format(topic_id))

plt.tight_layout()
plt.show()