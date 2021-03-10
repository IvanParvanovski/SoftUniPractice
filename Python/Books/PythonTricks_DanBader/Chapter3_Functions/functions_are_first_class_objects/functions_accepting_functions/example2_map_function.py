def yell(text):
    return text.upper() + '!'


bark = yell

print(list(map(bark, ['hello', 'hey', 'hi'])))
