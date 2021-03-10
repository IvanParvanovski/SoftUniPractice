from django.test import TestCase, Client
from django.urls import reverse

from testing.models import Profile


class PersonViewsTests(TestCase):
    def setUp(self):
        self.test_client = Client()

    def test_getIndex_whenNoProfiles_shouldRenderCorrectTemplateWithNoProfiles(self):
        response = self.test_client.get(reverse('profiles'))
        profiles = response.context['profiles']
        form = response.context['form']

        self.assertTemplateUsed(response, 'index.html')
        self.assertEqual(0, len(profiles))
        self.assertIsNotNone(form)

    def test_getIndex_whenTwoProfiles_shouldRenderCorrectTemplateWithTwoProfiles(self):
        profiles_create = (
            Profile(name='a', age=1, egn='1234567890'),
            Profile(name='b', age=2, egn='1234567890'),
        )
        [profile.save() for profile in profiles_create]

        response = self.test_client.get(reverse('profiles'))
        profiles = response.context['profiles']
        form = response.context['form']

        self.assertTemplateUsed(response, 'index.html')
        self.assertEqual(2, len(profiles))
        self.assertIsNotNone(form)

    def test_postIndex_whenValidEgn_shouldRedirectToIndex(self):
        name = 'Ivan'
        age = '15'
        egn = '1234567890'

        data = {
            'name': name,
            'age': age,
            'egn': egn,
        }
        response = self.test_client.post(reverse('profiles'), data=data)

        self.assertRedirects(response, reverse('profiles'))

    def test_postIndex_whenValidContainsLetters_shouldRenderIndexAndContainErrors(self):
        name = 'Ivan'
        age = '15'
        egn = '12345678a0'

        data = {
            'name': name,
            'age': age,
            'egn': egn,
        }
        response = self.test_client.get(reverse('profiles'), data=data)
        profiles = response.context['profiles']
        form = response.context['form']

        self.assertTemplateUsed(response, 'index.html')
        self.assertEqual(0, len(profiles))
        self.assertIsNotNone(form.errors)
