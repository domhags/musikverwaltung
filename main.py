from music_collection import MusicCollection
from track import Track
from album import Album


def main():
    collection = MusicCollection()

    while True:
        print("Musikverwaltung\n"
              "1. Album hinzufügen\n"
              "2. Album entfernen\n"
              "3. Song zu einem Album hinzufügen\n"
              "4. Song aus einem Album entfernen\n"
              "5. Alben anzeigen\n"
              "6. Beenden")

        choice = input("Wählen Sie eine Option: ")

        if choice == "1":
            title = input("Titel des Albums: ")
            interpret = input("Interpret des Albums: ")
            album = Album(title, interpret)
            collection.add_album(album)
            print(f"Album '{title}' hinzugefügt.")
        elif choice == "2":
            collection.print_album_title()
            title = input("Titel des zu entfernenden Albums: ")
            album = next((a for a in collection.albums if a.title == title), None)
            if album:
                collection.remove_album(album)
                print(f"Album '{title}' entfernt.")
            else:
                print(f"Album '{title}' nicht gefunden.")
        elif choice == "3":
            collection.print_album_title()
            album_title = input("Titel des Albums, zu dem der Song hinzugefügt werden soll: ")
            album = next((a for a in collection.albums if a.title == album_title), None)
            if album:
                song_title = input("Titel des Songs: ")
                filename = input("Dateiname des Songs: ")
                length = int(input("Länge des Songs in Sekunden: "))
                track = Track(song_title, filename, length)
                album.add_song(track)
                print(f"Song '{song_title}' zum Album '{album_title}' hinzugefügt.")
            else:
                print(f"Album '{album_title}' nicht gefunden.")
        elif choice == "4":
            collection.print_album_title()
            album_title = input("Titel des Albums, aus dem der Song entfernt werden soll: ")
            album = next((a for a in collection.albums if a.title == album_title), None)
            if album:
                collection.print_track_title()
                track_title = input("Titel des zu entfernenden Songs: ")
                track = next((t for t in album.tracks if t.title == track_title), None)
                if track:
                    album.remove_song(track)
                    print(f"Song '{track_title}' aus dem Album '{album_title}' entfernt.")
                else:
                    print(f"Song '{track_title}' im Album '{album_title}' nicht gefunden.")
            else:
                print(f"Album '{album_title}' nicht gefunden.")
        elif choice == "5":
            collection.print_albums()
        elif choice == "6":
            print("Programm beendet.")
            break
        else:
            print("Ungültige Auswahl. Bitte versuche es erneut.")


if __name__ == "__main__":
    main()
