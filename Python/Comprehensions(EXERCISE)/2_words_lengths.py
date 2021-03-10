words = input().split(", ")
words_length = [f"{word} -> {len(word)}" for word in words]
print(', '.join(words_length))
