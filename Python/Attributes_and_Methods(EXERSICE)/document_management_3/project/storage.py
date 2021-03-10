class Storage:
    def __init__(self):
        self.categories = list()
        self.topics = list()
        self.documents = list()

    def does_category_exist(self, category):
        return category in self.categories

    def does_topic_exist(self, topic):
        return topic in self.topics

    def does_document_exist(self, document):
        return document in self.documents

    def find_category(self, category_id):
        return [category for category in self.categories if category.id == category_id][0]

    def find_topic(self, topic_id):
        return [topic for topic in self.topics if topic.id == topic_id][0]

    def find_document(self, document_id):
        return [document for document in self.documents if document.id == document_id][0]

    def get_all_documents_in_string(self):
        result = ""
        for document in self.documents:
            result += f"{document}\n"
        return result

    # ---------- Main ----------

    def add_category(self, category):
        if self.does_category_exist(category):
            return

        self.categories.append(category)

    def add_topic(self, topic):
        if self.does_topic_exist(topic):
            return

        self.topics.append(topic)

    def add_document(self, document):
        if self.does_document_exist(document):
            return

        self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        current_category = self.find_category(category_id)
        current_category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        current_topic = self.find_topic(topic_id)
        current_topic.topic = new_topic
        current_topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        document = self.find_document(document_id)
        document.file_name = new_file_name

    def delete_category(self, category_id):
        category = self.find_category(category_id)
        self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = self.find_topic(topic_id)
        self.topics.remove(topic)

    def delete_document(self, document_id):
        document = self.find_document(document_id)
        self.documents.remove(document)

    def get_document(self, document_id):
        return self.find_document(document_id)

    def __repr__(self):
        return self.get_all_documents_in_string()
