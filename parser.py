import re
import nltk
from nltk.corpus import stopwords
from collections import Counter
from nltk.stem.wordnet import WordNetLemmatizer
import googletrans


class TextProcessor:
    def __init__(self):
        nltk.download('stopwords')
        nltk.download('wordnet')
        nltk.download('omw-1.4')
        nltk.download('averaged_perceptron_tagger')
        self.lemmatizer = WordNetLemmatizer()
        self.swords = set(stopwords.words("english"))
        fil = open("to_skip.txt")
        self.skip_words = [i[:-1] for i in fil.readlines()]
        fil.close()
        self.content = list()
        self.text = str()

    def parse_text(self, text):
        text = re.sub("[^a-zA-Z]", ' ', text)
        # print(f'Remove punctuation and numbers: {text}')

        text = text.lower().split()
        # print(f'Lowercase and split: {text}')

        text = [w for w in text if w not in self.swords]
        text = [w for w in text if w not in self.skip_words]
        # print(f'Remove stop words: {text}')
        text = " ".join(text)
        # print(f'Final: {text}')
        for word in text.split(" "):
            self.content.append(self.lemmatizer.lemmatize(word))
        # self.content.append(self.lemmatizer.lemmatize(text))

    def process(self):
        print(f'test = {self.content[:10]}')
        most_com = Counter(self.content).most_common(500)
        with open('freq_words.txt', 'w') as outfile:
            for word in most_com:
                outfile.write(word[0] + str(word[1]) + "\n")

    @classmethod
    def get_wordnet_pos(cls, word):
        """Map POS tag to first character lemmatize() accepts"""
        tag = nltk.pos_tag([word])[0][1][0].upper()
        tag_dict = {"J": wordnet.ADJ,
                    "N": wordnet.NOUN,
                    "V": wordnet.VERB,
                    "R": wordnet.ADV}

        return tag_dict.get(tag, wordnet.NOUN)

