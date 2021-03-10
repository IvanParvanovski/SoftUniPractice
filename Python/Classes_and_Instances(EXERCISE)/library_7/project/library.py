from collections import defaultdict


def is_new_username_identical(user, new_username):
    return user.username == new_username


class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = defaultdict(dict)

    def does_user_exist(self, user):
        return user in self.user_records

    def add_user(self, user):
        if self.does_user_exist(user):
            return f"User with id = {user.user_id} already registered in the library!"

        self.user_records.append(user)

    def remove_user(self, user):
        if not self.does_user_exist(user):
            return "We could not find such user to remove!"

        self.user_records.remove(user)

    def change_username(self, user_id: int, new_username: str):
        user_list = [user for user in self.user_records if user.user_id == user_id]

        if not user_list:
            return f"There is no user with id = {user_id}!"

        user = user_list[0]
        if is_new_username_identical(user, new_username):
            return "Please check again the provided username - it should be different than the username used so far!"

        user.username = new_username
        return f"Username successfully changed to: {new_username} for userid: {user_id}"
