from django import forms

class searchForm(forms.Form):
    sits = forms.CharField()
    date = forms.DateField()
    Country = forms.CharField()
    LocationName = forms.CharField()