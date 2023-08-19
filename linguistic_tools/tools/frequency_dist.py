from modules import *


class FrequencyDistribution():
    def __init__(self, sentences):
        self.sentences = str(sentences)
        self.frequency = self.Frequency()
    
    def Frequency(self):
        tokens = word_tokenize(self.sentences)
        dict_list = {}
        self.freq = FreqDist(tokens)
        return self.freq

    def __str__(self):
        """
        Word Frequency Distribution
        """

freq_obj = FrequencyDistribution("the mall is bigger than other malls but not bigger than my own mall")
for word, count in freq_obj.Frequency().items():
    print("[{}] == [{}]".format(word, count))