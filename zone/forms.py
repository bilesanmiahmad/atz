from django import forms
from django.utils.translation import ugettext_lazy as _

class EmailForm(forms.Form):
    first_name = forms.CharField(max_length=70, 
    widget=forms.TextInput(attrs={
        'class': 'form-control', 
        'placeholder': _('First Name')
        }))
    last_name = forms.CharField(max_length=70, 
    widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': _('Last Name')
        }))
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': _('Email')
            }))
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': _('Message')
            }))