from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User,Vehicle

class LoginForm(forms.Form):


    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_user', 'is_admin', 'is_superadmin')




class VehicleForm(forms.ModelForm):

    class Meta:
        model = Vehicle
        fields = ['vehicle_number', 'vehicle_type', 'vehicle_model', 'vehicle_description']

    vehicle_number = forms.CharField(widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    vehicle_model = forms.CharField(widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    vehicle_description = forms.CharField(widget=forms.Textarea(
            attrs={
                "class": "form-control"
            }
        )
    )

