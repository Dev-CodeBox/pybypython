from django import forms
from .models import Twix

class TwixForm(forms.ModelForm):
    class Meta:
        model = Twix
        fields = ['text', 'image',]