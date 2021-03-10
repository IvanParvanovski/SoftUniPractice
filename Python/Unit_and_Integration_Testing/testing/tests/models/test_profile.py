# Save to database
# from unittest import TestCase

# Does not save to database
from django.test import TestCase

from django.core.exceptions import ValidationError

from testing.models import Profile


class ProfileModelTests(TestCase):
    def test_creatProfile_whenValidEgn_shouldCreateTheProfile(self):
        name = 'Ivan'
        age = 15
        egn = '1234567890'
        profile = Profile(
            name=name,
            age=age,
            egn=egn,
        )

        profile.save()

    def test_creatProfile_whenEgnContainsLetters_shouldCreateTheProfile(self):
        name = 'Ivan'
        age = 15
        egn = 'W2E4J67M90'

        with self.assertRaises(ValidationError) as context:
            profile = Profile(
                name=name,
                age=age,
                egn=egn,
            )
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)
