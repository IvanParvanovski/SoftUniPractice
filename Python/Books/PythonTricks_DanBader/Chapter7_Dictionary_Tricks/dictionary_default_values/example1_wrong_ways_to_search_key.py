name_for_userid = {
    382: 'Alice',
    950: 'Bob',
    590: 'Dilbert',
}


def greeting1(userid):
    return 'Hi %s!' % name_for_userid[userid]


def greeting2(userid):
    if userid in name_for_userid:
        return 'Hi %s!' % name_for_userid[userid]
    else:
        return 'Hi there!'


print(greeting2(382))
print(greeting2(500))

print()

print(greeting1(382))
print(greeting1(500))

