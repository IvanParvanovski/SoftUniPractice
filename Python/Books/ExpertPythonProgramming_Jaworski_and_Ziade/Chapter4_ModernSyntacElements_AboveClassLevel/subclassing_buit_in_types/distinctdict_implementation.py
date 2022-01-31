from collections import UserDict


class DistinctError(ValueError):
    """Raised when duplicate values is added to a distinctdict."""
    pass


class distinctdict(UserDict):
    """Dictionary that does not accept duplicate values."""
    def __setitem__(self, key, value):
        if value in self.values():
            if (
                (key in self and self[key] != value)
                or key not in self
            ):
              raise DistinctError('This value already exists for different key')

        super().__setitem__(key, value)


my = distinctdict()
my['key'] = 'value'
# my['other_key'] = 'value'

my['other_key'] = 'value2'
