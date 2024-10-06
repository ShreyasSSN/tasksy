from django import forms
from . import models

class AddScreenShot(forms.ModelForm):
    class Meta:
        model  =models.UserData
        fields = ['screenshot']