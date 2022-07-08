from django import forms
from .models import URL

class UrlShortForm(forms.ModelForm):
    class Meta:
        model = URL
        fields = ['url_long']
