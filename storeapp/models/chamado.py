# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from storeapp.models import Produto
from storeapp.models.imagem import Imagem


class Chamado(models.Model):
    '''
    :param nome: models.CharField(max_length=200, verbose_name="Extensão",
                                help_text='Tipo de arquivo (Exemplo: PDF, DOC ou DOCX).')
    :param usuario: models.ForeignKey(User, verbose_name="Usuário")
    :param excluido: models.BooleanField(default=False, verbose_name="Excluído")
    :param desativado: models.BooleanField(default=False)
    '''
    # cod = models.CharField(max_length=200,unique=True, verbose_name="Codigo do Chamado")
    cod = models.CharField(max_length=200, verbose_name="Codigo do Chamado")
    descricao = models.TextField(max_length=200, verbose_name="Nome do Produto",
                                help_text='Nome do Produto (Exemplo: Leite, Ovo , etc .).')
    usuario = models.ForeignKey(User, verbose_name="Usuário",on_delete=False)
    funcionario = models.ForeignKey(User, verbose_name="Funcionario",on_delete=False,
                                    help_text='Funcionario que está solicitando o conserto.',
                                   related_name='funcionario_usuario')
    responsavel = models.ForeignKey(User, verbose_name="Usuário",on_delete=False,
                                    help_text='Funcionario responsavel pelo conserto.',
                                   related_name='responsavel_usuario')

    produto_utilizado= models.ManyToManyField(Produto, blank=True)
    imagem = models.ManyToManyField(Imagem, blank=True)
    data_inicio = models.DateTimeField(auto_now=True, null=True)
    data_fim = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(default=False)
    excluido = models.BooleanField(default=False, verbose_name="Excluído")
    desativado = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s' % self.cod

    def get_absolute_url(self):
        return reverse('chamado-detail', kwargs={'pk': self.pk})

    class Meta:
        app_label = "storeapp"
        verbose_name = 'Chamado'
        verbose_name_plural = 'Chamados'
        permissions = (
            ("store_add_chamado", "Adicionar chamado"),
            ("store_detail_chamado", "Visualizar chamado"),
        )
