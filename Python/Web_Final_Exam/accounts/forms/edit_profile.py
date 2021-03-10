from django import forms

from accounts.models import UserProfile


class ProfileEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    username = forms.CharField(max_length=150)

    class Meta:
        model = UserProfile
        exclude = ('user', )

