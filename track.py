class Track:
    def __init__(self, title, filename, length):
        self.title = title
        self.filename = filename
        self.length = length

    def __str__(self):
        return f"{self.title} [{self.format_time(self.length)}]"

    @staticmethod
    def format_time(sec):
        minutes, sec = divmod(sec, 60)
        hours, minutes = divmod(minutes, 60)
        return f"{hours:02}:{minutes:02}:{sec:02}"
