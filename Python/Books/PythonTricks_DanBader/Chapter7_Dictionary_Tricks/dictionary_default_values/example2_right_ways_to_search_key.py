name_for_userid = {
    382: 'Alice',
    950: 'Bob',
    590: 'Dilbert',
}


def greeting1(userid):
    try:
        return 'Hi %s!' % name_for_userid[userid]
    except KeyError:
        return 'Hi there!'


def greeting2(userid):
    return 'Hi %s!' % name_for_userid.get(userid, 'there')


print(greeting2(382))
print(greeting2(500))

print()

print(greeting1(382))
print(greeting1(500))
