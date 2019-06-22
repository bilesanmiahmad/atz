from django import forms

class EmailForm(forms.Form):
    first_name = forms.CharField(max_length=70, 
    widget=forms.TextInput(attrs={
        'class': 'form-control', 
        'placeholder': 'First Name'
        }))
    last_name = forms.CharField(max_length=70, 
    widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Last Name'
        }))
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email'
            }))
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Message'
            }))