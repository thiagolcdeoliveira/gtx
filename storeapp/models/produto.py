# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from .tipo_produto import TipoProduto
from .categoria import Categoria
from .status import Status

#from .garantia import Garantia

from .item import Item

class Produto(models.Model):
    '''
    :param nome: models.CharField(max_length=200, verbose_name="Extensão",
                                help_text='Tipo de arquivo (Exemplo: PDF, DOC ou DOCX).')
    :param usuario: models.ForeignKey(User, verbose_name="Usuário")
    :param excluido: models.BooleanField(default=False, verbose_name="Excluído")
    :param desativado: models.BooleanField(default=False)
    '''

    nome = models.CharField(max_length=200, verbose_name="Nome do Produto",
                                help_text='Nome do Produto (Exemplo: Leite, Ovo , etc .).')
    codigo_barras = models.CharField(max_length=200, verbose_name="Código de Barras",
                                     help_text='Código de Barras (Exemplo: 000001).')
    tipo_produto = models.ForeignKey(TipoProduto, on_delete=False,verbose_name="Tipo de Produto.",
                                     help_text='Tipo de Produto: Selecione um tipo de produto (Exemplo: Estoque).')
    complemento_nome = models.CharField(max_length=200, verbose_name="Complemento do Nome",
                                        help_text='Complemento do Nome (Exemplo: Não sei).')



    #mg_venda = models.FloatField(max_length=200, verbose_name="Mg. Venda",
    #                                    help_text='Mg. Venda (Exemplo: Não sei).')
    categoria = models.ForeignKey(Categoria,on_delete=False, verbose_name="Complemento do Nome",
                                        help_text='Complemento do Nome (Exemplo: Não sei).', blank=True, null=True)




    status = models.ForeignKey(Status,on_delete=False, verbose_name="Status",
                            help_text='Status (Exemplo: .).')



    imagem = models.FileField(upload_to='media/produto/', verbose_name="Imagem",
                            help_text='Imagem (Exemplo:  .).', blank=True)

   # garantia = models.ForeignKey(Garantia,on_delete=False, verbose_name="Garantia",
    #                        help_text='Garantia (Exemplo:  .).')

    item = models.ManyToManyField(Item, verbose_name="Itens Extras",
                            help_text='Itens Extras(Exemplo: Leite, Ovo , etc .).')
    usuario = models.ForeignKey(User, verbose_name="Usuário",on_delete=False)
    excluido = models.BooleanField(default=False, verbose_name="Excluído")
    desativado = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s' % self.nome

    def get_absolute_url(self):
        # return reverse('produto-detail', kwargs={'id': self.pk})
        return reverse('produto-detail', kwargs={'pk': self.pk})

    class Meta:
        app_label = "storeapp"
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        permissions = (
            ("store_add_produto", "Adicionar Produto"),
            ("store_detail_produto", "Visualizar Produto"),
        )
