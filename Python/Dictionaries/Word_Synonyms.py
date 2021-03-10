words_count = int(input())
synonym_dict = dict()

for _ in range(words_count):
    word = input()
    synonym = input()

    if word not in synonym_dict:
        synonym_dict[word] = list()
    synonym_dict[word].append(synonym)

for word in synonym_dict:
    print(f"{word} - {', '.join(synonym_dict[word])}")