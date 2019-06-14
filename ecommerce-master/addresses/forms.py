from django import forms
from django.forms import ModelForm, Textarea
from .models import Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = [
            'phone',
            'address',
            'city',
            'country',
            'state',
            'postal_code'
        ]
        widgets = {
            'phone'         : forms.TextInput(attrs={"class":"form-control","placeholder":"Your mobile number"}),
            'address'       : forms.TextInput(attrs={"class":"form-control","placeholder":"Your address"}),
            'city'          : forms.TextInput(attrs={"class":"form-control","placeholder":"Your city"}),
            'country'       : forms.TextInput(attrs={"class":"form-control"}),
            'state'         : forms.TextInput(attrs={"class":"form-control","placeholder":"Your state"}),
            'postal_code'   : forms.TextInput(attrs={"class":"form-control","placeholder":"Your postal code"})
        }
