from stat_parser import Parser 

#load the parser
parser = Parser()

class Parse():
    def __init__(self, sentence):
        self.sentence = str(sentence)
    
    def parse_sent(self):
        parsed = parser.parse(self.sentence)
        return parsed

sentence = input(">> Setence : ")
parse_obj = Parse(sentence)
print(parse_obj.parse_sent())