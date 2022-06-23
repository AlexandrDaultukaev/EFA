from googletrans import Translator
import pymorphy2

class PTranslator:
    def __init__(self, language='ru'):
        self.translator = Translator()
        self.lang = language
        self.morph = pymorphy2.MorphAnalyzer()

    def set_normal_form(self, text):
        ctx = list()
        for word in text.split("\n"):
            ctx.append(self.morph.parse(word)[0].normal_form)
        return ctx

    def trans(self):
        with open("freq_ru.txt", 'w') as wfile:
            with open("freq_words.txt") as file:
                content = file.read()
                content_ru = self.translator.translate(content, dest='ru')
            wfile.write(content_ru.text)



