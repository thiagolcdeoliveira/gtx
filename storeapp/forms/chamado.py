# -*- coding: utf-8 -*-
from django.forms import *
from storeapp.models.chamado import Chamado


class ChamadoForm(ModelForm):
    class Meta:
        model = Chamado
        exclude = ('usuario', 'excluido','cod','imagem','data_inicio','data_fim','status','produtos_utilizado', 'desativado')


class ChamadoUpdateForm(ModelForm):
    class Meta:
        model = Chamado
        exclude = ('usuario', 'excluido','cod', 'imagem','data_inico','data_fim','desativado')
