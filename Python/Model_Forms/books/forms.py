from django import forms
from django.core.exceptions import ValidationError

from books.models import Book


class BookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_form_control_class_to_all_fields()

    def add_form_control_class_to_all_fields(self):
        for (_, field) in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    # Validators
    def clean_pages(self):
        pages = self.cleaned_data['pages']
        if pages <= 0:
            raise ValidationError(f'Pages should be a positive number, now they are {pages}')
        return pages

    def clean_title(self):
        title = self.cleaned_data['title']
        if title[0].islower():
            raise ValidationError(f'Title first letter should be upper. :)')

        return title

    class Meta:
        model = Book
        fields = '__all__'

        # widgets = {
        #     'title': forms.TextInput(
        #         attrs={
        #           'class': 'form-control',
        #         },
        #     ),
        #
        #     'pages': forms.NumberInput(
        #         attrs={
        #           'class': 'form-control',
        #         },
        #     ),
        #
        #     'author': forms.TextInput(
        #         attrs={
        #             'class': 'form-control',
        #         },
        #     ),
        #
        #     'description': forms.Textarea(
        #         attrs={
        #             'class': 'form-control',
        #         },
        #     ),
        # }
