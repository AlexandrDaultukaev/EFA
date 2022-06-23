from subtitles_parser import YouTubeParser
from parser import TextProcessor
from translator import PTranslator
import re

class MainBody:
    def __init__(self):
        self.direct = {}
        self.ids = []

    def get_translate(self):
        youtube_parser = YouTubeParser()
        preproc = TextProcessor()
        translator = PTranslator()
        youtube_parser.parse(self.ids)
        preproc.parse_text(youtube_parser.origin)
        preproc.process()
        translator.trans()

    def set_link(self, links):
        for i in range(len(links)):
            self.ids.append(re.sub(r'[a-zA-Z:.?!@#$%^&*()]+//[a-zA-Z:.?!@#$%^&*()]+/', '', links[i]))
        print(self.ids)



if __name__ == '__main__':
    mb = MainBody()
    link = ['https://youtu.be/x9TQ6culXIA','https://youtu.be/LnlKwzc_TNA','https://youtu.be/00NgUctWoLQ']
    mb.set_link(link)
    mb.get_translate()