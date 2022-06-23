from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import Formatter
from youtube_transcript_api.formatters import TextFormatter
from parser import TextProcessor


# assigning srt variable with the list
# of dictonaries obtained by the get_transcript() function

class YouTubeParser:
    def __init__(self):
        self.origin = str()


    def parse(self, ids):
        formatter = TextFormatter()
        for i in range(len(ids)):
            srt = YouTubeTranscriptApi.get_transcript(ids[i])
            self.origin += formatter.format_transcript(srt) + ' '


