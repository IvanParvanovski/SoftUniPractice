
from django import forms

from testing.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        # widgets = {
        #     'name': forms.TextInput(
        #         attrs={
        #             'class': 'test'
        #         },
        #     ),
        # }
