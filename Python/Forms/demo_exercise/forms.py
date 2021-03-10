from django import forms


def min_validator(value):
    if not value or len(value) < 10:
        raise forms.ValidationError(f'Value should be more than 10, now it is {len(value)} :)')


class DemoExerciseForm(forms.Form):
    bot_catcher = forms.CharField(
        widget=forms.HiddenInput,
        required=False
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ), max_length=30)

    age = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
            }
        ),
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
            }
        ),
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        ),
    )

    size = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                'type': 'range',
            }
        ),
    )

    text = forms.CharField(
        widget=forms.Textarea,
        required=False,
        label='Comments',
    )

    def clean_bot_catcher(self):
        if len(self.cleaned_data['bot_catcher']):
            raise forms.ValidationError('This is a bot')


class DemoExerciseFormFull(forms.Form):
    bot_catcher = forms.CharField(
        widget=forms.HiddenInput,
        required=False
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    name = forms.CharField(max_length=30)
    age = forms.IntegerField(widget=forms.NumberInput)
    email = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)

    size = forms.IntegerField(
        widget=forms.TextInput(
            attrs={'type': 'range'}
        ),
    )

    text = forms.CharField(
        widget=forms.Textarea,
        required=False,
        label='Comments',
        validators=(
            min_validator,
        )
    )

    def clean_bot_catcher(self):
        if len(self.cleaned_data['bot_catcher']):
            raise forms.ValidationError('This is a bot')
