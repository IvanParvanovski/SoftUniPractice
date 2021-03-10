from django import forms

from templates_advanced_app.models import Python


class PythonCreateForm(forms.ModelForm):

    class Meta:
        model = Python
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(
                attrs={
                    'class': 'my-class',
                },
            ),
        }


class FilterForm(forms.Form):
    ORDER_ASC = 'asc'
    ORDER_DESC = 'desc'

    ORDER_CHOICES = (
        (ORDER_ASC, 'Ascending'),
        (ORDER_ASC, 'Descending')
    )

    text = forms.CharField(required=False)
    order = forms.ChoiceField(choices=ORDER_CHOICES, required=False)
