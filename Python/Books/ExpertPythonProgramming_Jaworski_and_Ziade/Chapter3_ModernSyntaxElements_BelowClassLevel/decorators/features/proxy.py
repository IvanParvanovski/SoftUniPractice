class User:
    def __init__(self, roles):
        self.roles = roles


class Unauthorized(Exception):
    pass


def protect(role):
    def _protect(function):
        def __protect(*args, **kwargs):
            user_ = globals().get('user')
            if user_ is None or role not in user_.roles:
                raise Unauthorized('I wont\'t tell you!')
            return function(*args, **kwargs)
        return __protect
    return _protect


class RecipeVault:
    @protect('admin')
    def get_waffle_recipe(self):
        print('use tons of buter!')


tarek = User(('admin', 'user'))
bill = User(('user',))

my_vault = RecipeVault()

user = tarek
my_vault.get_waffle_recipe()

user = bill
my_vault.get_waffle_recipe()
