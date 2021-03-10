def get_speak_func(volume):
    def whisper(text):
        return text.lower() + '...'

    def yell(text):
        return text.upper() + '!'

    if volume > 0.5:
        return yell
    else:
        return whisper


yell_func = get_speak_func(10)
whisper_func = get_speak_func(0.2)

print(yell_func)
print(whisper_func)

print('----------------------')

print(yell_func('Hello, World'))
print(whisper_func('Hello, World'))
