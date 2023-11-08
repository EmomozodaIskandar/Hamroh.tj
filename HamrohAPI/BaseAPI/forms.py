from django.forms import forms
from .models import *


# Form that created for User model 
class UserForm(forms.Form):
    class Meta:
        model = User
        fields = '__all__'