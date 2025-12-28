from django import forms
from django.forms import ModelForm, DateInput

from .models import Aluno

class AlunoForm(forms.ModelForm):

    class Meta:
        model = Aluno
        exclude = ['data_criacao', 'ultima_modificacao', 'data_evento']
        fields = '__all__'
