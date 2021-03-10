def yell(text):
    return text.upper() + '!'


def whisper(text):
    return text.lower() + '...'


bark = yell


def greet(func):
    greeting = func('Hi, I am a Python program')
    print(greeting)


greet(bark)
greet(whisper)