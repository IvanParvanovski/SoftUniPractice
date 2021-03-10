def speak(text):
    def whisper(t):
        return t.lower() + '...'
    return whisper(text)


print(speak('Hello, World'))
print(whisper('Hello, World!'))