from django import forms
from .models import Todolistmodels

class Todolistform(forms.ModelForm):
    class Meta:
        model=Todolistmodels
        fields=["task","done"]