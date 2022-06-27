from calendar import c
from dataclasses import field
from pyexpat import model
from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from passagens.classe_viagem import tipo_de_classes
from passagens.validation import *
from passagens.models import ClasseViagem, Pessoa, Passagem

class PassagemForms(forms.ModelForm):


    data_pesquisa = forms.DateField(label='Data da pesquisa', disabled=True, initial=datetime.today())

    class Meta:
        model = Passagem
        fields = '__all__'
        labels = {
            'data_ida': 'Data de ida',
            'data_volta': 'Data de volta',
            'informacoes': 'Informações',
            'classe_viagem': 'Classe da Viagem',
            'data_pesquisa': 'Data da pesquisa',
        }

        widgets = {
            'data_ida': DatePicker(),
            'data_volta': DatePicker(),
        }
        
    
    def clean(self):
        origem = self.cleaned_data.get('origem')
        destino = self.cleaned_data.get('destino')
        data_ida = self.cleaned_data.get('data_ida')
        data_volta = self.cleaned_data.get('data_volta')
        data_pesquisa = self.cleaned_data.get('data_pesquisa')
        lista_de_erros = {}

        campo_tem_algum_numero(origem, 'origem', lista_de_erros)
        campo_tem_algum_numero(destino, 'destino', lista_de_erros)
        origem_destino_iguais(origem, destino, lista_de_erros)
        data_de_volta_menor_que_data_de_ida(data_ida, data_volta, lista_de_erros)
        data_de_ida_menor_que_data_de_hoje(data_ida, data_pesquisa, lista_de_erros)

        if lista_de_erros is not None:

            for erro in lista_de_erros:
                mensagem_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_erro)

        return self.cleaned_data


class PessoaForms(forms.ModelForm):
    class Meta:
        model = Pessoa
        exclude = ['nome']