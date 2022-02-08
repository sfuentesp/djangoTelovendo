
from django import forms
from django.db.models import fields
from proveedor.models import Proveedor



class ProveeFormLogin(forms.ModelForm):
    class Meta:
        model=Proveedor
        fields=("username","password")


class LoginForm(forms.Form):
    nombre=forms.CharField(widget=forms.TextInput)
    password=forms.CharField(widget=forms.PasswordInput)


        