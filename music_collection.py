from album import Album


class MusicCollection:
    def __init__(self):
        self.albums = []

    def add_album(self, album):
        if not isinstance(album, Album):
            print("Das hinzuzufügende Objekt ist kein gültiges Album.")
            return
        if album.title in [a.title for a in self.albums]:
            print(f"Album '{album.title}' ist bereits in der Sammlung enthalten.")
            return
        self.albums.append(album)
        print(f"Album '{album.title}' hinzugefügt.")

    def remove_album(self, album):
        if not isinstance(album, Album):
            print("Das zu entfernende Objekt ist kein gültiges Album.")
            return
        if album in self.albums:
            self.albums.remove(album)
            print(f"Album '{album.title}' entfernt.")
        else:
            print(f"Album '{album.title}' nicht in der Sammlung gefunden.")

    def print_albums(self):
        if not self.albums:
            print(f"Keine Alben gefunden")
        else:
            for album in self.albums:
                print(album)

    def print_album_title(self):
        if not self.albums:
            print("Keine Alben in der Sammlung.")
        for album in self.albums:
            print(f" {album.title}")

    def print_track_title(self):
        if not self.albums:
            print("Keine Alben in der Sammlung.")
            return
        track_titles = []
        for album in self.albums:
            for track in album.tracks:
                track_titles.append(track.title)
        if track_titles:
            print("Tracks in der Sammlung:")
            for title in track_titles:
                print(f" {title}")
        else:
            print("Keine Tracks in der Sammlung.")
