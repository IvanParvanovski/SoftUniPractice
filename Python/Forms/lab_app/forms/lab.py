from django import forms

from lab_app.form_validators.lab import NameValidator


class LabForm(forms.Form):
    pk = forms.CharField(
        widget=forms.HiddenInput(),
        required=False
    )

    bot_catcher = forms.CharField(
        widget=forms.HiddenInput,
        required=False,
    )

    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            },
        ),

        validators=(
            NameValidator().validate,

        ),
    )

    age = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control'
            },
        ),

        validators=(

        ),
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
            },
        ),

        validators=(

        ),
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            },
        ),

        validators=(

        ),
    )

    text = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
            },
        ),

        validators=(

        ),
    )

    def clean_bot_catcher(self):
        if self.cleaned_data['bot_catcher']:
            raise forms.ValidationError('This is a bot!')
