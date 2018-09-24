from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class UserRegistrateForm(forms.Form):
    username = forms.CharField(
                        label='Username',
                        max_length=255,
                        min_length=5,
                        widget=forms.TextInput(attrs={'class': 'username_cls', 'placeholder': 'Username ...'})
    )

    # username = forms.CharField(label='Username',max_length=255)
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'email_cls', 'placeholder': 'Email ...'}))
    #email = forms.EmailField(label='Email')
    password = forms.CharField(
                        label='Password',
                        max_length=255,
                        min_length=5,
                        widget=forms.PasswordInput(attrs={'class': 'password_cls', 'placeholder': 'Password ...'})

    )
    #password = forms.CharField(label='Password', max_length=255)


    def clean_email(self):
        email = self.cleaned_data['email']
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise ValidationError('Email is already registerd.')
        return email
