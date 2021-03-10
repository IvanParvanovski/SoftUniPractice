class Album:
    def __init__(self, name: str, *songs):
        self.name = name
        self.songs = list(songs)
        self.published = False

    def does_song_exist(self, song):
        return song in self.songs

    def is_song_single(self, song):
        return song.single

    def add_song(self, song):
        if self.published:
            return "Cannot add songs. Album is published."

        if self.does_song_exist(song):
            return "Song is already in the album."

        if self.is_song_single(song):
            return f"Cannot add {song.name}. It's a single"

        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        songs = [song for song in self.songs if song.name == song_name]

        if self.published:
            return "Cannot remove songs. Album is published."

        if not songs:
            return "Song is not in the album."

        self.songs.remove(songs[0])
        return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."

        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        output = f"Album {self.name}\n"

        for song in self.songs:
            output += f"== {song.get_info()}\n"

        return output
