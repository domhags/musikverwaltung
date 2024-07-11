from track import Track


class Album:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.tracks = []

    def add_track(self, track):
        if not isinstance(track, Track):
            return "Das hinzuzufügende Objekt ist kein gültiger Track."

        if track.title in [t.title for t in self.tracks]:
            return f"Track '{track.title}' ist bereits im Album '{self.title}' enthalten."

        self.tracks.append(track)
        return f"Track '{track.title}' zum Album '{self.title}' hinzugefügt."

    def remove_track(self, track):
        if not isinstance(track, Track):
            return "Das zu entfernende Objekt ist kein gültiger Track."

        if track in self.tracks:
            self.tracks.remove(track)
            return f"Track '{track.title}' aus dem Album '{self.title}' entfernt."
        else:
            return f"Track '{track.title}' im Album '{self.title}' nicht gefunden."

    def total_length(self):
        total_seconds = sum(track.length for track in self.tracks)
        return self.format_time(total_seconds)

    def __str__(self):
        album_info = f"Album: {self.title}\nVon: {self.artist}\nLänge: {self.total_length()}"
        if self.tracks:
            album_info += "\n\n"
            for index, track in enumerate(self.tracks, start=1):
                album_info += f"Track {index}: {str(track)}\n"
        return album_info.strip()

    @staticmethod
    def format_time(sec):
        minutes, sec = divmod(sec, 60)
        hours, minutes = divmod(minutes, 60)
        return f"{hours:02}:{minutes:02}:{sec:02}"

    def print_track_titles(self):
        if not self.tracks:
            return f"Album '{self.title}' enthält keine Tracks."
        else:
            result = [f"Tracks im Album '{self.title}':"]
            for index, track in enumerate(self.tracks, start=1):
                result.append(f"{index}. {track.title}")
            return "\n".join(result)
