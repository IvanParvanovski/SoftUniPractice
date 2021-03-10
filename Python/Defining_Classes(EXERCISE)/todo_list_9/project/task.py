from typing import List


class Task:
    def __init__(self, name: str, due_date: str):
        self.name = name
        self.due_date = due_date

        self.comments: List[str] = list()
        self.completed = False

    def is_new_name_valid(self, new_name: str) -> bool:
        return new_name != self.name

    def is_new_due_date_valid(self, new_date: str) -> bool:
        return new_date != self.due_date

    def is_new_comment_index_valid(self, index: int) -> bool:
        return 0 <= index < len(self.comments)

    def change_name(self, new_name: str) -> str:
        if not self.is_new_name_valid(new_name):
            return "Name cannot be the same."

        self.name = new_name
        return new_name

    def change_due_date(self, new_date: str) -> str:
        if not self.is_new_due_date_valid(new_date):
            return "Date cannot be the same."

        self.due_date = new_date
        return new_date

    def add_comment(self, comment: str) -> None:
        self.comments.append(comment)

    def edit_comment(self, comment_number: int, new_comment: str) -> str:
        if not self.is_new_comment_index_valid(comment_number):
            return "Cannot find comment."

        self.comments[comment_number] = new_comment
        return ', '.join(self.comments)

    def details(self):
        return f"Name: {self.name} - Due Date: {self.due_date}"
