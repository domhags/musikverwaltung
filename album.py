class Album:
    def __init__(self, title, interpret):
        self.title = title
        self.interpret = interpret
        self.tracks = []

    def add_song(self, track):
        self.tracks.append(track)

    def remove_song(self, track):
        self.tracks.remove(track)

    def total_length(self):
        total_seconds = sum(track.length for track in self.tracks)
        return self.format_time(total_seconds)

    def __str__(self):
        album_info = f"Album: {self.title}\nVon: {self.interpret}\nLänge: {self.total_length()}"
        if self.tracks:
            album_info += "\n\n"
            for index, track in enumerate(self.tracks, start=1):
                album_info += f"Song {index}: {str(track)}\n"
        return album_info.strip()

    @staticmethod
    def format_time(sec):
        minutes, sec = divmod(sec, 60)
        hours, minutes = divmod(minutes, 60)
        return f"{hours:02}:{minutes:02}:{sec:02}"
