words = input().split()
user_word = input()
palindromes = list()


def palindromes_equality(word):
    if word == word[::-1]:
        return word


for word in words:
    if palindromes_equality(word) is not None:
        palindromes.append(palindromes_equality(word))

print(palindromes)
print(f"Found palindrome {palindromes.count(user_word)} times")
