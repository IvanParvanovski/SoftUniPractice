def palindrome(word, index):
    if index == int(len(word) / 2):
        return f"{word} is a palindrome"

    if word[index] != word[-index - 1]:
        return f"{word} is not a palindrome"

    return palindrome(word, index + 1)
