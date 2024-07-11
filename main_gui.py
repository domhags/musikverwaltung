import tkinter as tk
from tkinter import messagebox, ttk
from album import Album
from music_collection import MusicCollection
from track import Track


class MusicApp:
    def __init__(self, main_windows):
        self.main_windows = main_windows
        self.main_windows.title("Musikverwaltung")
        self.main_windows.geometry("600x400")

        self.collection = MusicCollection()

        self.main_frame = tk.Frame(self.main_windows)
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        self.main_windows.grid_rowconfigure(0, weight=1)
        self.main_windows.grid_columnconfigure(0, weight=1)

        self.show_main_menu()

    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def show_main_menu(self):
        self.clear_frame()

        # Hauptmenü-Buttons
        tk.Button(self.main_frame, text="Album hinzufügen",
                  command=self.add_album).grid(row=0, column=0, padx=10, pady=5)
        tk.Button(self.main_frame, text="Album entfernen",
                  command=self.delete_album).grid(row=0, column=1, padx=10, pady=5)
        tk.Button(self.main_frame, text="Track hinzufügen",
                  command=self.add_track_to_album).grid(row=1, column=0, padx=10, pady=5)
        tk.Button(self.main_frame, text="Track entfernen",
                  command=self.remove_track_from_album).grid(row=1, column=1, padx=10, pady=5)
        tk.Button(self.main_frame, text="Alle Alben anzeigen",
                  command=self.display_all_albums).grid(row=2, column=0, padx=10, pady=5)
        tk.Button(self.main_frame, text="Album auswählen/anzeigen",
                  command=self.display_selected_album).grid(row=2, column=1, padx=10, pady=5)
        tk.Button(self.main_frame, text="Beenden",
                  command=self.main_windows.quit).grid(row=3, column=0, columnspan=2, padx=10, pady=5)

    def add_album(self):
        self.clear_frame()

        # Labels und Eingabefelder für Album hinzufügen
        tk.Label(self.main_frame, text="Album hinzufügen").grid(row=0, columnspan=2, pady=10)

        title_label = tk.Label(self.main_frame, text="Titel")
        title_label.grid(row=1, column=0, padx=10, pady=5)
        title_entry = tk.Entry(self.main_frame)
        title_entry.grid(row=1, column=1, padx=10, pady=5)

        artist_label = tk.Label(self.main_frame, text="Interpret")
        artist_label.grid(row=2, column=0, padx=10, pady=5)
        artist_entry = tk.Entry(self.main_frame)
        artist_entry.grid(row=2, column=1, padx=10, pady=5)

        def save_album():
            # Album speichern und zurück zum Hauptmenü
            title = title_entry.get().strip()
            artist = artist_entry.get().strip()
            if not title or not artist:
                messagebox.showerror("Fehler", "Titel und Interpret dürfen nicht leer sein.")
                return
            album = Album(title, artist)
            self.collection.add_album(album)
            messagebox.showinfo("Erfolg", f"Album '{title}' hinzugefügt.")
            self.show_main_menu()

        tk.Button(self.main_frame, text="Speichern",
                  command=save_album).grid(row=3, columnspan=2, padx=10, pady=5)
        tk.Button(self.main_frame, text="Zurück",
                  command=self.show_main_menu).grid(row=4, columnspan=2, padx=10, pady=5)

    def delete_album(self):
        # Funktion zum Löschen eines Albums
        self.clear_frame()
        tk.Label(self.main_frame, text="Album entfernen").grid(row=0, columnspan=2, pady=10)

        if not self.collection.albums:
            messagebox.showinfo("Information", "Es sind keine Alben vorhanden.")
            self.show_main_menu()
            return

        album_titles = [album.title for album in self.collection.albums]

        tk.Label(self.main_frame, text="Wählen Sie ein Album").grid(row=1, column=0, padx=10, pady=5)
        album_combobox = ttk.Combobox(self.main_frame, values=album_titles)
        album_combobox.grid(row=1, column=1, padx=10, pady=5)

        def remove_album():
            # Methode für den Löschvorgang eines Albums
            selected_album_title = album_combobox.get().strip()
            album = next((a for a in self.collection.albums if a.title == selected_album_title), None)

            if album:
                self.collection.remove_album(album)
                messagebox.showinfo("Erfolg", f"Album '{selected_album_title}' entfernt.")
            else:
                messagebox.showerror("Fehler", f"Album '{selected_album_title}' nicht gefunden.")

            self.show_main_menu()

        tk.Button(self.main_frame, text="Entfernen",
                  command=remove_album).grid(row=2, columnspan=2, padx=10, pady=5)
        tk.Button(self.main_frame, text="Zurück",
                  command=self.show_main_menu).grid(row=3, columnspan=2, padx=10, pady=5)

    def add_track_to_album(self):
        self.clear_frame()
        # Hinzufügen eines Tracks zu einem Album
        tk.Label(self.main_frame, text="Track zu Album hinzufügen").grid(row=0, columnspan=2, pady=10)

        if not self.collection.albums:
            messagebox.showinfo("Information", "Es sind keine Alben vorhanden.")
            self.show_main_menu()
            return

        album_titles = [album.title for album in self.collection.albums]

        tk.Label(self.main_frame, text="Wählen Sie ein Album").grid(row=1, column=0, padx=10, pady=5)
        album_combobox = ttk.Combobox(self.main_frame, values=album_titles)
        album_combobox.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.main_frame, text="Tracktitel").grid(row=2, column=0, padx=10, pady=5)
        track_title_entry = tk.Entry(self.main_frame)
        track_title_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.main_frame, text="Dateiname (*.mp3)").grid(row=3, column=0, padx=10, pady=5)
        filename_entry = tk.Entry(self.main_frame)
        filename_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(self.main_frame, text="Länge in Sekunden").grid(row=4, column=0, padx=10, pady=5)
        length_entry = tk.Entry(self.main_frame)
        length_entry.grid(row=4, column=1, padx=10, pady=5)

        def save_track():
            # Track wird gespeichert
            album_title = album_combobox.get().strip()
            track_title = track_title_entry.get().strip()
            filename = filename_entry.get().strip()
            length_str = length_entry.get().strip()

            if not album_title or not track_title or not filename or not length_str:
                messagebox.showerror("Fehler", "Alle Felder müssen ausgefüllt sein.")
                return

            if not self.is_mp3_file(filename):
                messagebox.showerror("Fehler", "Dateiname muss die Endung '.mp3' haben.")
                return

            try:
                length = int(length_str)
                if length <= 0:
                    raise ValueError("Länge muss eine positive Zahl sein.")
            except ValueError:
                messagebox.showerror("Fehler", "Ungültige Länge.")
                return

            album = next((a for a in self.collection.albums if a.title == album_title), None)

            if album:
                track = Track(track_title, filename, length)
                album.add_track(track)
                messagebox.showinfo("Erfolg", f"Track '{track_title}' zum Album '{album_title}' hinzugefügt.")
            else:
                messagebox.showerror("Fehler", f"Album '{album_title}' nicht gefunden.")

            self.show_main_menu()

        tk.Button(self.main_frame, text="Speichern",
                  command=save_track).grid(row=5, columnspan=2, padx=10, pady=5)
        tk.Button(self.main_frame, text="Zurück",
                  command=self.show_main_menu).grid(row=6, columnspan=2, padx=10, pady=5)

    def remove_track_from_album(self):
        self.clear_frame()
        # Methode zum Entfernen eines Songs von einem Album
        tk.Label(self.main_frame, text="Track aus Album entfernen").grid(row=0, columnspan=2, pady=10)

        if not self.collection.albums:
            messagebox.showinfo("Information", "Es sind keine Alben vorhanden.")
            self.show_main_menu()
            return

        album_titles = [album.title for album in self.collection.albums]

        tk.Label(self.main_frame, text="Wählen Sie ein Album").grid(row=1, column=0, padx=10, pady=5)
        album_combobox = ttk.Combobox(self.main_frame, values=album_titles)
        album_combobox.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.main_frame, text="Wählen Sie einen Track").grid(row=2, column=0, padx=10, pady=5)
        track_combobox = ttk.Combobox(self.main_frame)
        track_combobox.grid(row=2, column=1, padx=10, pady=5)

        def update_track_list():
            selected_album_title = album_combobox.get().strip()
            album = next((a for a in self.collection.albums if a.title == selected_album_title), None)

            if album:
                track_titles = [track.title for track in album.tracks]
                track_combobox['values'] = track_titles
            else:
                track_combobox['values'] = []

        # Hier werden für jedes ausgewählte Album die Tracks aktualisiert und angezeigt
        album_combobox.bind("<<ComboboxSelected>>", lambda event: update_track_list())

        tk.Label(self.main_frame, text="Wählen Sie einen Track").grid(row=2, column=0, padx=10, pady=5)
        track_combobox = ttk.Combobox(self.main_frame)
        track_combobox.grid(row=2, column=1, padx=10, pady=5)

        def remove_track():
            # Hier wird der Track entfernt
            selected_album_title = album_combobox.get().strip()
            selected_track_title = track_combobox.get().strip()

            if not selected_album_title or not selected_track_title:
                messagebox.showerror("Fehler", "Wählen Sie ein Album und einen Track aus.")
                return

            album = next((a for a in self.collection.albums if a.title == selected_album_title), None)

            if album:
                track = next((t for t in album.tracks if t.title == selected_track_title), None)
                if track:
                    album.remove_track(track)
                    messagebox.showinfo("Erfolg", f"Track '{selected_track_title}' aus Album '"
                                                  f"{selected_album_title}' entfernt.")
                else:
                    messagebox.showerror("Fehler", f"Track '{selected_track_title}' nicht gefunden "
                                                   f"in Album '{selected_album_title}'.")
            else:
                messagebox.showerror("Fehler", f"Album '{selected_album_title}' nicht gefunden.")

            self.show_main_menu()

        tk.Button(self.main_frame, text="Entfernen",
                  command=remove_track).grid(row=3, columnspan=2, padx=10, pady=5)
        tk.Button(self.main_frame, text="Zurück",
                  command=self.show_main_menu).grid(row=4, columnspan=2, padx=10, pady=5)

    def display_all_albums(self):
        self.clear_frame()
        # Methode zum Anzeigen aller Alben in einem Textfeld
        tk.Label(self.main_frame, text="Alben anzeigen").grid(row=0, columnspan=2, pady=10)

        if not self.collection.albums:
            messagebox.showinfo("Information", "Es sind keine Alben vorhanden.")
            self.show_main_menu()
            return

        text_widget = tk.Text(self.main_frame, wrap=tk.WORD, width=70, height=10)
        text_widget.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Schleife über alle Alben und zum Textfeld hinzufügen
        for idx, album in enumerate(self.collection.albums):
            text_widget.insert(tk.END, f"Album: {album.title}\n")
            text_widget.insert(tk.END, f"Interpret: {album.artist}\n")
            album_length = sum(track.length for track in album.tracks)
            minutes, seconds = divmod(album_length, 60)
            text_widget.insert(tk.END, f"Länge: {minutes:02}:{seconds:02}\n")
            text_widget.insert(tk.END, "\n")  # Leerzeile für bessere Lesbarkeit

        tk.Button(self.main_frame, text="Zurück",
                  command=self.show_main_menu).grid(row=2, columnspan=2, padx=10, pady=5)
        text_widget.config(state=tk.DISABLED)  # Textfeld ist nur lesbar

    def display_selected_album(self):
        self.clear_frame()
        tk.Label(self.main_frame, text="Ausgewähltes Album anzeigen").grid(row=0, columnspan=2, pady=10)

        if not self.collection.albums:
            messagebox.showinfo("Information", "Es sind keine Alben vorhanden.")
            self.show_main_menu()
            return

        album_titles = [album.title for album in self.collection.albums]

        tk.Label(self.main_frame, text="Wählen Sie ein Album").grid(row=1, column=0, padx=10, pady=5)
        album_combobox = ttk.Combobox(self.main_frame, values=album_titles)
        album_combobox.grid(row=1, column=1, padx=10, pady=5)

        text_widget = tk.Text(self.main_frame, wrap=tk.WORD, width=70, height=10)
        text_widget.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # Funktion zur Aktualisierung des ausgewählten Albums
        def update_selected_album(event=None):
            selected_album_title = album_combobox.get().strip()

            if not selected_album_title:
                # Wenn kein Album ausgewählt ist, Text Widget leeren
                text_widget.config(state=tk.NORMAL)
                text_widget.delete('1.0', tk.END)
                text_widget.config(state=tk.DISABLED)
                return

            album = next((a for a in self.collection.albums if a.title == selected_album_title), None)

            if album:
                text_widget.config(state=tk.NORMAL)
                text_widget.delete('1.0', tk.END)

                text_widget.insert(tk.END, f"Album: {album.title}\n")
                text_widget.insert(tk.END, f"Von: {album.artist}\n")
                album_length = sum(track.length for track in album.tracks)
                minutes, seconds = divmod(album_length, 60)
                text_widget.insert(tk.END, f"Länge: {minutes:02}:{seconds:02}\n\n")

                for idx, track in enumerate(album.tracks, start=1):
                    track_length = track.length
                    track_minutes, track_seconds = divmod(track_length, 60)
                    text_widget.insert(tk.END, f"Track {idx}: {track.title} [{track_minutes:02}:{track_seconds:02}]\n")

                text_widget.config(state=tk.DISABLED)
            else:
                messagebox.showerror("Fehler", f"Album '{selected_album_title}' nicht gefunden.")

        # Initialisierung der Anzeige, wenn ein Album ausgewählt wird
        album_combobox.bind("<<ComboboxSelected>>", update_selected_album())
        update_selected_album()  # Einmaliges Update, um das erste Album anzuzeigen

        tk.Button(self.main_frame, text="Zurück",
                  command=self.show_main_menu).grid(row=3, columnspan=2, padx=10, pady=5)

    @staticmethod
    def is_mp3_file(filename):
        return filename.lower().endswith('.mp3')


if __name__ == "__main__":
    root = tk.Tk()
    app = MusicApp(root)
    root.mainloop()
