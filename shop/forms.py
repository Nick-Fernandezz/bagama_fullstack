from django import forms
from phonenumber_field.formfields import PhoneNumberField
from django.contrib.auth.forms import AuthenticationForm



class RegisterForm(forms.Form):

    name = forms.CharField(max_length=50, min_length=2, label='Введите имя', required=True, widget=forms.TextInput(attrs={'placeholder': ' '}))
    phonenumber = PhoneNumberField(widget=forms.TextInput(attrs={'placeholder': (' ')}), 
                       label=("Введите телефон"), required=True)
    email = forms.EmailField(max_length=100, min_length=2, label='Введите e-mail', required=True, widget=forms.TextInput(attrs={'placeholder': ' '}), )
    password1 = forms.CharField(
        label=("Введите пароль"),
        widget=forms.PasswordInput(attrs={"placeholder": " "}),
    )
    password2 = forms.CharField(
        label=("Повторите пароль"),
        widget=forms.PasswordInput(attrs={"placeholder": " "}),
    )
