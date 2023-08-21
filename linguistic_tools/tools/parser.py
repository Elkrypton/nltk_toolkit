from stat_parser import Parser 
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.tag import pos_tag
import nltk


def create_custom_parse()
#load the parser
parser = Parser()

class Parse():
    def __init__(self, sentence):
        self.sentence = str(sentence)
    
    def parse_sent(self):
        parsed = parser.parse(self.sentence)
        return parsed


class CustomParser():
    def __init__(self, document):
        self.document = document
    
    def sentence_parser(self):
        self.sentence_tokens = sent_tokenize(self.document)
        return self.sentence_tokens
    
    def word_parser(self):
        self.word_tokens =  [word_tokenize(w) for w in self.sentence_tokens]
        return self.word_tokens
    
    def pos_tagger(self):
        self.pos_tags = [pos_tag(w) for w in self.word_tokens]
        return self.pos_tags
    
    def parse(self):
        self.sentence_tokens = self.sentence_parser()
        self.word_tokens = self.word_parser()
        self.pos_tags = self.pos_tagger()
        return self.pos_tags

def parse_chart(tagged):
    tagged = tagged
    grammar = "NP: {<DT>?<JJ>*<NN>?<NNP>?<NN>}"
    cp = nltk.RegexpParser(grammar)
    parsed = cp.parse(tagged)
    return parsed
    

    
if __name__ == "__main__":
    sentence = "I like to eat chicken"
    tagged = [("DT", "I"), ("JJ", "like"), ("NN", "to"), ("VP", "eat"), ("NN", "chicken")]
    parsed = parse_chart(tagged)
    print(parsed)
    parsed.draw()
    #parser = CustomParser(sentence)
    # print(parser.parse())
    # print(parser.parse_tree(tagged))
    # print(parser.parse_chart())

    