class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = list()

    def does_album_exist(self, album):
        return album in self.albums

    def add_album(self, album):
        if self.does_album_exist(album):
            return f"Band {self.name} already has {album.name} in their library."

        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        albums = [album for album in self.albums if album.name == album_name]

        if not albums:
            return f"Album {album_name} is not found."

        album = albums[0]
        if album.published:
            return "Album has been published. It cannot be removed."

        self.albums.remove(album)
        return f"Album {album_name} has been removed."

    def details(self):
        output = f"Band {self.name}\n"

        for album in self.albums:
            output += f"{album.details()}\n"

        return output
