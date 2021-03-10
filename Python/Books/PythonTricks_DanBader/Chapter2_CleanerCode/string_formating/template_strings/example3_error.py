from string import Template

SECRET = 'this-is-a-secret'


class Error:
    def __init__(self):
        pass


error = Error()
user_input = '$error.__init__.__globals__[SECRET]'
print(Template(user_input).substitute(error=error))
# print(user_input.format(error=error))



