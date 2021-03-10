class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [list() for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(photos_count // 4)

    def add_photo(self, label: str):
        for page_index in range(len(self.photos)):
            page = self.photos[page_index]

            if len(page) < 4:
                self.photos[page_index].append(label)
                return f"{label} photo added successfully on page" \
                       f" {page_index + 1} slot {len(page)}"
        return "No more free spots"

    def display(self):
        result = "-----------\n"
        for page in self.photos:
            result += f"{'[] ' * len(page) if len(page) > 0 else ' '}"
            result = result[:-1]
            result += "\n-----------\n"
        return result

