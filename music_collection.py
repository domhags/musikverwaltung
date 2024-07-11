from album import Album


class MusicCollection:
    def __init__(self):
        self.albums = []

    def add_album(self, album):
        if not isinstance(album, Album):
            return "Das hinzuzufügende Objekt ist kein gültiges Album."

        if album.title in [a.title for a in self.albums]:
            return f"Album '{album.title}' ist bereits in der Sammlung enthalten."

        self.albums.append(album)
        return f"Album '{album.title}' hinzugefügt."

    def remove_album(self, album):
        if not isinstance(album, Album):
            return "Das zu entfernende Objekt ist kein gültiges Album."

        if album in self.albums:
            self.albums.remove(album)
            return f"Album '{album.title}' entfernt."
        else:
            return f"Album '{album.title}' nicht in der Sammlung gefunden."

    def print_albums(self):
        if not self.albums:
            return f"Keine Alben gefunden"
        else:
            for album in self.albums:
                return album

    def print_album_title(self):
        if not self.albums:
            return "Keine Alben in der Sammlung."
        for album in self.albums:
            return f" {album.title}"

    def print_track_titles(self):
        if not self.albums:
            return "Keine Alben in der Sammlung."

        track_titles = []
        for album in self.albums:
            for track in album.tracks:
                track_titles.append(track.title)

        if track_titles:
            return "Tracks in der Sammlung:\n" + "\n".join(f" - {title}" for title in track_titles)
        else:
            return "Keine Tracks in der Sammlung."
