from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm
from django.contrib.auth.models import User

#Registration Form here......
class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password(Again)', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'first_name:First Name', 'last_name:Last Name', 'email:Email'}
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'}),
                   'first_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'last_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'email': forms.EmailInput(attrs={'class': 'form-control'}),
                   }


#login form here............
class LoginForm(AuthenticationForm):
    username =UsernameField(widget=forms.TextInput(attrs={'class':'form-control','autofocus':True}))
    password =forms.CharField(label="Password",strip=False,widget=forms.PasswordInput(attrs={'class':'form-control','autocomplete':'current-password'}))


#Password change form here....................
class ChangePass(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1 = forms.CharField(label='New Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2 = forms.CharField(label='New Password(Again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))

