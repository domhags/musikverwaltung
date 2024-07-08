from music_collection import MusicCollection
from track import Track
from album import Album


def main():
    collection = MusicCollection()

    while True:
        print("Musikverwaltung\n"
              "1. Album hinzufügen\n"
              "2. Album entfernen\n"
              "3. Track zu einem Album hinzufügen\n"
              "4. Track aus einem Album entfernen\n"
              "5. Alben anzeigen\n"
              "6. Beenden")

        choice = input("Wählen Sie eine Option: ").strip()

        if choice == "1":
            title = input("Titel des Albums: ").strip()
            interpret = input("Interpret des Albums: ").strip()
            if not title or not interpret:
                print("Titel und Interpret dürfen nicht leer sein.")
                continue
            album = Album(title, interpret)
            collection.add_album(album)

        elif choice == "2":
            if not collection.albums:
                print("Keine Alben in der Sammlung.")
                continue
            collection.print_album_title()
            title = input("Titel des zu entfernenden Albums: ").strip()
            album = next((a for a in collection.albums if a.title == title), None)
            if album:
                collection.remove_album(album)
            else:
                print(f"Album '{title}' nicht gefunden.")

        elif choice == "3":
            if not collection.albums:
                print("Keine Alben in der Sammlung.")
                continue
            collection.print_album_title()
            album_title = input("Titel des Albums, zu dem der Track hinzugefügt werden soll: ").strip()
            album = next((a for a in collection.albums if a.title == album_title), None)
            if album:
                track_title = input("Titel des Tracks: ").strip()
                filename = input("Dateiname des Tracks: ").strip()
                length_input = input("Länge des Tracks in Sekunden: ").strip()
                if not track_title or not filename or not length_input:
                    print("Tracktitel, Dateiname und Länge dürfen nicht leer sein.")
                    continue
                if not length_input.isdigit():
                    print("Länge muss eine gültige Zahl sein.")
                    continue
                length = int(length_input)
                if length <= 0:
                    print("Länge muss eine positive Zahl sein.")
                    continue
                track = Track(track_title, filename, length)
                album.add_track(track)
            else:
                print(f"Album '{album_title}' nicht gefunden.")

        elif choice == "4":
            if not collection.albums:
                print("Keine Alben in der Sammlung.")
                continue
            collection.print_album_title()
            album_title = input("Titel des Albums, aus dem der Track entfernt werden soll: ").strip()
            album = next((a for a in collection.albums if a.title == album_title), None)
            if album:
                if not album.tracks:
                    print(f"Album '{album_title}' enthält keine Tracks.")
                    continue
                album.print_track_titles()
                track_title = input("Titel des zu entfernenden Tracks: ").strip()
                track = next((t for t in album.tracks if t.title == track_title), None)
                if track:
                    album.remove_track(track)
                else:
                    print(f"Track '{track_title}' im Album '{album_title}' nicht gefunden.")
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
