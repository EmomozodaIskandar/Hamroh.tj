from django import forms
from .models import Locations

class searchForm(forms.Form):
    sits = forms.CharField()
    date = forms.DateField()
    class Meta: 
        model = Locations
        fields = ['__all__'] 