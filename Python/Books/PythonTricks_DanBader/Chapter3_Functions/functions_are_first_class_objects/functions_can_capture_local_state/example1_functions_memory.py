def get_speak_func(text, volume):
    # REMEMBERS 'Hello'
    def whisper():
        return text.lower() + '...'

    def yell():
        return text.upper() + '!'

    if volume > 0.5:
        return yell
    else:
        return whisper


my_func = get_speak_func('Hello', 0.5)
print(my_func())
