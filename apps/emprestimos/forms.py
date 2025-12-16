from django import forms
from django.forms import ModelForm, DateInput

from .models import Emprestimo

class EmprestimoForm(forms.ModelForm):

    class Meta:
        model = Emprestimo
        exclude = ['data_emprestimo',]
        fields = '__all__'
