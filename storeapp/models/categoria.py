# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Categoria(models.Model):
    '''
    :param nome: models.CharField(max_length=200, verbose_name="Extensão",
                                help_text='Tipo de arquivo (Exemplo: PDF, DOC ou DOCX).')
    :param usuario: models.ForeignKey(User, verbose_name="Usuário")
    :param excluido: models.BooleanField(default=False, verbose_name="Excluído")
    :param desativado: models.BooleanField(default=False)
    '''
    nome = models.CharField(max_length=200, verbose_name="Nome da Categoria",
                                help_text='Nome da Categoria (Exemplo: .).')
    descricao = models.CharField(max_length=200, verbose_name="Descrição",
                            help_text='Descrição (Exemplo: .).')
    quantidade = models.PositiveIntegerField( verbose_name="Quantidade",
                            help_text='Quantidade (Exemplo: .).')
    principal = models.CharField(max_length=200, verbose_name="Principal",
                            help_text='Principal (Exemplo: .).')
    unidade = models.CharField(max_length=200, verbose_name="Unidade",
                            help_text='Unidade (Exemplo: .).')
    secundaria = models.CharField(max_length=200, verbose_name="Secundária",
                            help_text='Secundária (Exemplo:  .).')
    fabricante = models.CharField(max_length=200, verbose_name="Nome do Fabricante",
                            help_text='Nome do Fabricante (Exemplo: Leite, Ovo , etc .).')
    secao = models.CharField(max_length=200, verbose_name="Seção/Categoria",
                            help_text='Seção/Categoria (Exemplo: Leite, Ovo , etc .).')
    grupo = models.CharField(max_length=200, verbose_name="Gruṕo",
                            help_text='Grupo (Exemplo:  .).')
    grade_produto = models.CharField(max_length=200, verbose_name="Grade de Produtos",
                            help_text='Grade de Produtos (Exemplo:  .).')

    usuario = models.ForeignKey(User, verbose_name="Usuário",on_delete=False)

    excluido = models.BooleanField(default=False, verbose_name="Excluído")
    desativado = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s' % self.nome

    def get_absolute_url(self):
        return reverse('produto-detail', kwargs={'pk': self.pk})

    class Meta:
        app_label = "storeapp"
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        permissions = (
            ("store_add_produto", "Adicionar Produto"),
            ("store_detail_produto", "Visualizar Produto"),
        )
