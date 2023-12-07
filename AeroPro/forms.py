
from django import forms
from .models import *

class PassagemForm(forms.ModelForm):
    class Meta:
        model = Passagem
        fields = '__all__'

class PilotoForm(forms.ModelForm):
    class Meta:
        model = Piloto
        fields = '__all__'

class ComissarioForm(forms.ModelForm):
    class Meta:
        model = Comissario
        fields = '__all__'

class AeronaveForm(forms.ModelForm):
    class Meta:
        model = Aeronave
        fields = '__all__'

class PassageiroForm(forms.ModelForm):
    class Meta:
        model = Passageiro
        fields = '__all__'

class CompanhiaAereaForm(forms.ModelForm):
    class Meta:
        model = CompanhiaAerea
        fields = '__all__'

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = '__all__'

class VooForm(forms.ModelForm):
    class Meta:
        model = Voo  # Substitua 'SeuModelo' pelo nome real do seu modelo
        fields = '__all__'  # Ou liste os campos que deseja incluir, excluindo 'passagens'
        exclude = ['passagens']