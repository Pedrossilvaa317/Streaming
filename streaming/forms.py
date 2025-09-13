from django.forms import ModelForm
from .models import Filmes
from django import forms


class FilmeForm(forms.ModelForm):
    class Meta:
        model = Filmes
        fields = ['titulo', 'genero', 'ano_lancamento', 'plataformas']
        widgets = {
            'plataformas': forms.CheckboxSelectMultiple
        }
