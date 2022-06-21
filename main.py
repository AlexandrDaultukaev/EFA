from subtitles_parser import YouTubeParser
from parser import TextProcessor
from translator import PTranslator
import re

class MainBody:
    def __init__(self):
        self.direct = {}
        self.id = int()

    def get_translate(self):
        youtube_parser = YouTubeParser()
        preproc = TextProcessor()
        translator = PTranslator()
        youtube_parser.parse(self.id)
        preproc.parse_text(youtube_parser.origin)
        preproc.process()
        translator.trans()

    def set_link(self, link):
        self.id = re.sub(r'[a-zA-Z:.?!@#$%^&*()]+//[a-zA-Z:.?!@#$%^&*()]+/', '', link)
        print(self.id)



if __name__ == '__main__':
    mb = MainBody()
    mb.set_link("https://youtu.be/3jS_yEK8qVI")
    mb.get_translate()