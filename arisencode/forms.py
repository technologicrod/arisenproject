from django import forms
from .models import List
from django.core.exceptions import ValidationError


class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['name', 'gender', 'age']
