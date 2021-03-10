from django import forms

from exam_app.forms.common import DisabledFormMixin
from exam_app.models.recipe import Recipe


class RecipeCreateForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'


class DisabledRecipeForm(RecipeCreateForm,
                         DisabledFormMixin):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        DisabledFormMixin.__init__(self)
