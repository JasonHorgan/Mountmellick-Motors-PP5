from django import forms
from .models import Stock


class ProductForm(forms.ModelForm):

    class Meta:
        model = Stock
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
