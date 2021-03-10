from django import forms

from profile_app.models.profile import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'budget': forms.NumberInput(),
            'first_name': forms.TextInput(),
            'last_name': forms.TextInput(),
        }
