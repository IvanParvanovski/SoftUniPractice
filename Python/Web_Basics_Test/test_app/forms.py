from django import forms

from test_app.models import FormTest


class FormTestCreateForm(forms.ModelForm):
    class Meta:
        model = FormTest
        fields = '__all__'
        widgets = {
            'gender': forms.RadioSelect(),
            'cars': forms.CheckboxSelectMultiple(),
        }
