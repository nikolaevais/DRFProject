from rest_framework.serializers import ValidationError
import re


class YoutubeValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        youtube = re.compile("youtube.com")
        tmp_val = dict(value).get(self.field)
        if not bool(youtube.search(tmp_val)):
            raise ValidationError("Указанный сайт нельзя использовать")