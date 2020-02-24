# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Imagem(models.Model):
    '''
    :param nome: models.CharField(max_length=200, verbose_name="Extensão",
                                help_text='Tipo de arquivo (Exemplo: PDF, DOC ou DOCX).')
    :param usuario: models.ForeignKey(User, verbose_name="Usuário")
    :param excluido: models.BooleanField(default=False, verbose_name="Excluído")
    :param desativado: models.BooleanField(default=False)
    '''
    imagem = models.CharField(max_length=200, verbose_name="Nome do Produto",
                                help_text='Nome do Produto (Exemplo: Leite, Ovo , etc .).')
    usuario = models.ForeignKey(User, verbose_name="Usuário",on_delete=False)

    excluido = models.BooleanField(default=False, verbose_name="Excluído")
    desativado = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s' % self.usuario

    def get_absolute_url(self):
        return reverse('produto-detail', kwargs={'pk': self.pk})

    class Meta:
        app_label = "storeapp"
        verbose_name = 'Imagem'
        verbose_name_plural = 'Imagens'
        permissions = (
            ("store_add_imagem", "Adicionar imagem"),
            ("store_detail_imagens", "Visualizar imagem"),
        )
