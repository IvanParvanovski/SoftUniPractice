class Comment:
    def __init__(self, username, content, likes=0):
        self.user_name = username
        self.user_content = content
        self.user_likes = likes


comment = Comment("user1", "I like this book")
print(comment.user_name)
print(comment.user_content)
print(comment.user_likes)
