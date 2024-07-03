class MusicCollection:
    def __init__(self):
        self.albums = []

    def add_album(self, album):
        self.albums.append(album)

    def remove_album(self, album):
        self.albums.remove(album)

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
            print(album.title)

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
                print(title)
        else:
            print("Keine Tracks in der Sammlung.")
