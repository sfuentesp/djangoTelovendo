
from django import forms
from django.db.models import fields
from .models import Proveedor


class ProveeForm(forms.ModelForm):
    class Meta:
        model=Proveedor
        fields=("rut","nombre","dire","telefono")
        