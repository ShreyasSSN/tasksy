from django import forms
from . import models
from .get_logo import get_logo_and_save

class AddApplication(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddApplication, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.label = ''

    class Meta:
        model = models.Application
        fields = ["app_name", "app_link", "app_category", "app_subcategories", "app_points"]
        widgets = {
            'app_name': forms.TextInput(attrs={'placeholder': 'App Name'}),
            'app_link': forms.TextInput(attrs={'placeholder': 'App Link'}),
            'app_category': forms.Select(attrs={'placeholder': 'App Category'}),
            'app_subcategories': forms.Select(attrs={'placeholder': 'App Sub Category'}),
            'app_points': forms.NumberInput(attrs={'placeholder': 'App points'}),
        }
