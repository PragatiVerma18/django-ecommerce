from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class GuestForm(forms.Form):
    email     = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"Your email"}))

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Your username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Your password"}))

class RegisterForm(forms.Form):
    username  = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Your username"}))
    phone     = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Your mobile number"}))
    email     = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"Your email"}))
    password  = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Your password"}))
    password2 = forms.CharField(label="Confirm password",widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Confirm your password"}))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username is taken")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email is taken")
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password2!=password:
            raise forms.ValidationError("Passwords must match")
        return data
