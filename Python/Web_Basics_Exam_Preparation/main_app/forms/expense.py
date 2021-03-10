from django import forms

from main_app.forms.common import DisabledFormMixin
from main_app.models.expense import Expense


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(),
            'description': forms.Textarea(),
            'image_url': forms.URLInput(),
            'price': forms.NumberInput(),
        }


class DeleteExpenseForm(ExpenseForm, DisabledFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        DisabledFormMixin.__init__(self)
