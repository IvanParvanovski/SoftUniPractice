class Document:
    def __init__(self,
                 id: int,
                 category_id: int,
                 topic_id: int,
                 file_name: str):

        self.id = id
        self.category_id = category_id
        self.topic_id = topic_id
        self.file_name = file_name
        self.tags = list()

    @classmethod
    def from_instances(cls,
                       id: int,
                       category,
                       topic,
                       file_name: str):

        return cls(id, category.id, topic.id, file_name)

    def does_tag_already_exist(self, tag):
        return tag in self.tags

    def add_tag(self, tag_content: str):
        if self.does_tag_already_exist(tag_content):
            return

        self.tags.append(tag_content)

    def remove_tag(self, tag_content: str):
        if not self.does_tag_already_exist(tag_content):
            return

        self.tags.remove(tag_content)

    def edit(self, file_name: str):
        self.file_name = file_name

    def __repr__(self):
        return f"Document {self.id}: {self.file_name}; " \
               f"category {self.category_id}, topic {self.topic_id}," \
               f" tags: {', '.join(self.tags)}"
