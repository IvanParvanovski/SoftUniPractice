name = 'Ivan'
errno = 50159747054

print(
    'Hey %(name)s, there is a 0x%(errno)x error!' %
    {
        "name": name,
        "errno": errno,
    }
)
