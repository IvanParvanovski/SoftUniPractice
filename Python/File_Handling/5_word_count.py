import re


def get_words_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read().split()


def get_words_from_text(line, words_count_dict):
    for word in words_count_dict:
        if word in line.lower():
            pattern = rf'[\s|\-|\.|\_|]{word}[\s|\-|\.|\_|\,]'
            words_count_dict[word] += len(re.findall(pattern, line.lower()))

    return words_count_dict


def get_words_count(file_path, words):
    words_counts = {word: 0 for word in words}
    with open(file_path, 'r') as file:
        for line in file:
            words_counts = get_words_from_text(line, words_counts)

    return words_counts


words_file_path = "files/Words Count/words.txt"
text_file_path = "files/Words Count/text.txt"

words_count = get_words_count(text_file_path, get_words_from_file(words_file_path))
sorted_words_count = sorted(words_count, key=lambda x: -words_count[x])
[print(f"{word} - {words_count[word]}") for word in sorted_words_count]
