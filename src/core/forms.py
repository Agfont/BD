from django import forms

CHARFIELD_LENGTH = 100

class ConflictForm(forms.Form):
    codigo = forms.IntegerField()
    nome = forms.CharField(max_length=CHARFIELD_LENGTH)
    tipo = forms.CharField(max_length=CHARFIELD_LENGTH)
    num_feridos = forms.IntegerField()
    num_mortos = forms.IntegerField()