import re
import nltk
from nltk.corpus import stopwords
from collections import Counter
content = []


nltk.download('stopwords')
swords = set(stopwords.words("english"))

fil = open('to_skip.txt', 'r')
skip_words = [i[:-1] for i in fil.readlines()]
fil.close()

print(skip_words)

def parse_text(text):
    # print(f'Input: {text}')

    text = re.sub("[^a-zA-Z]", ' ', text)
    # print(f'Remove punctuation and numbers: {text}')

    text = text.lower().split()
    # print(f'Lowercase and split: {text}')
    
    text = [w for w in text if w not in swords]
    text = [w for w in text if w not in skip_words]
    # print(f'Remove stop words: {text}')

    text = " ".join(text)
    # print(f'Final: {text}')

    return text

with open("parsed.txt") as file:
  content = file.readlines()
  # print(content)

text = str()

for i in range(len(content)):
  content[i] = parse_text(content[i])
  if(content[i]) == '\n' or (content[i]) == ' ' or content[i] == '':
    continue
  text += content[i] + " "

data = text.split(" ")
del data[-1]
# print(data)
most_com = Counter(data).most_common(1000)
with open('freq_words.txt', 'w') as outfile:
    for i in most_com:

        outfile.write(i[0]+"\n")




# tokenizer = Tokenizer(num_words = 100)
# tokenizer.fit_on_texts(content)
# word_index = tokenizer.word_index
# for k,v in word_index.items():
  # print(f"{k}: {v}\n")