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
        for i in self.content:
            if i == '\n' or i == ' ' or i == '':
                continue
            self.text += i + " "
            most_com = Counter(self.text.split(" ")).most_common(1000)
            with open('freq_words.txt', 'w') as outfile:
                for word in most_com:
                    outfile.write(word[0] + "\n")
