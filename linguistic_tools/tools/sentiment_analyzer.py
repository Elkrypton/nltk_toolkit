import nltk
import nltk.sentiment.util
import nltk.sentiment.sentiment_analyzer
from nltk.sentiment.vader import SentimentIntensityAnalyzer


class AdvancedSentimentAnalyzer():

    def __init__(self, sentences):
        self.sentences = sentences
    def Analyze(self):
        sentiment_model = SentimentIntensityAnalyzer()
        print("---BUILTIN SENTIMENT ANALYZER USING NLTK----")
        for sentence in self.sentences:
            print("[{}]".format(sentence), "\n -->")
            kvp = sentiment_model.polarity_scores(sentence)
            for k in kvp:
                print("{} -- {}".format(k,kvp[k]), '\n')
            print()

if __name__ == "__main__":
    sentences = ["worldwar is crazy", "Struggle us real as has been said by my old colleague"]
    analyze = AdvancedSentimentAnalyzer(sentences)
    analyze.Analyze()
    
    