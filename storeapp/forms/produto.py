# -*- coding: utf-8 -*-
from django.forms import *
from storeapp.models.produto import Produto


class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        exclude = ('usuario', 'excluido', 'desativado')

