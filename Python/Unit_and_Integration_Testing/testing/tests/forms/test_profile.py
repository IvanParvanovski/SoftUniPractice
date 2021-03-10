from django.test import TestCase

from testing.forms.profile import ProfileForm


class ProfileFormTests(TestCase):
    def test_saveProfileForm_whenValidEgn_shouldBeValid(self):
        name = 'Ivan'
        age = 15
        egn = '1234567890'
        form = ProfileForm(data={
            'name': name,
            'age': age,
            'egn': egn
        })

        self.assertTrue(form.is_valid())

    def test_saveProfileForm_whenEgnContainsLetters_shouldBeInvalid(self):
        name = 'Ivan'
        age = 15
        egn = '123a5d7w90'
        form = ProfileForm(data={
            'name': name,
            'age': age,
            'egn': egn
        })

        self.assertFalse(form.is_valid())

    def test_saveProfileForm_whenEgnContainsOnlyDigitsBut9_shouldBeInvalid(self):
        name = 'Ivan'
        age = 15
        egn = '123456789'
        form = ProfileForm(data={
            'name': name,
            'age': age,
            'egn': egn
        })

        self.assertFalse(form.is_valid())

    def test_saveProfileForm_whenEgnContainsOnlyDigitsBut11_shouldBeInvalid(self):
        name = 'Ivan'
        age = 15
        egn = '12345678912'
        form = ProfileForm(data={
            'name': name,
            'age': age,
            'egn': egn
        })

        self.assertFalse(form.is_valid())
