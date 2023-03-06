
from django import forms
from .models import *

class CustomerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['identification'].required = True

    class Meta:
        model = Customer
        fields = (
            'category',
            'code',
            'identification',
            'first_names',
            'last_names',
            'gender',
            'city',
            'address',
            'telephone',
            'email'
        )
        widgets = {
            'gender': forms.Select(attrs={
                'class': 'form-select',
                'required': True
            }),
            'category': forms.Select(attrs={
                'class': 'form-select',
                'required': True
            })
        }
