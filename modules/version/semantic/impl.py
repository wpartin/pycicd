from datetime import datetime

from modules.version.interface import Version


class SemanticVersion(Version):

    @classmethod
    def generate(cls):
        now = datetime.now()

        year = now.strftime("%y")
        month = now.strftime("%m")
        millis = str(int(now.timestamp() * 1000))[7:]

        return f"{year}.{month}.{millis}"
