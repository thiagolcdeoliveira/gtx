# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from .tipo_produto import TipoProduto
from .categoria import Categoria
from .carga_tributaria import CargaTributaria
from .tipo_credito import TipoCredito
from .natureza_receita import NaturezaReceita
from .tipo_item import TipoItem
from .tara_balanca import TaraBalanca
from .status import Status
from .tipo_venda import TipoVenda
from .embalagem_compra import EmbalagemCompra
from .comissao import Comissao
from .garantia import Garantia
from .vasilhame import Vasilhame
from .categoria_ecomerce import CategoriaEComerce
from .cest import Cest
from .anp import Anp
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
    nome_ecf = models.CharField(max_length=200, verbose_name="Nome ECF",
                                     help_text='Nome ECF (Exemplo: Não sei).')
    ncm = models.IntegerField( verbose_name="NCM",
                                        help_text='NCM (Exemplo: Não sei).')

    referencia = models.CharField(max_length=200, verbose_name="Referência",
                                        help_text='Rederência (Exemplo: Não sei ).')
    mg_venda = models.FloatField(max_length=200, verbose_name="Mg. Venda",
                                        help_text='Mg. Venda (Exemplo: Não sei).')
    categoria = models.ForeignKey(Categoria,on_delete=False, verbose_name="Complemento do Nome",
                                        help_text='Complemento do Nome (Exemplo: Não sei).')

    #Tributos loja data ini fim editar

    grade_tributaria_venda = models.ForeignKey(CargaTributaria,on_delete=False, related_name='GradeTributariaVendas', verbose_name="Grade Tributaria de Vendas  ",
                                  help_text='Grade Tributaria de Vendas (Exemplo: Não sei).')
    grade_devolucao_venda =   models.ForeignKey(CargaTributaria,on_delete=False, related_name='GradeTributariaDevolucao', verbose_name="Grade Devolução de Vendas ",
                                help_text='Grade Devolução de vendas (Exemplo: .).')
    tipo_credito = models.ForeignKey(TipoCredito, on_delete=False, verbose_name="Tipo Creditos",
                            help_text='Tipo Credito (Exemplo: .).')
    natureza_receita = models.ForeignKey(NaturezaReceita, on_delete=False, verbose_name="Natureza da Receita",
                            help_text='Natureza da Receita (Exemplo:  .).')
    #Paramentro

    tipo_item = models.ForeignKey(TipoItem,on_delete=False, verbose_name="Tipo Item",
                            help_text='Tipo Item (Exemplo:.).')
    validade = models.CharField(max_length=200, verbose_name="Validade",
                            help_text='Tecla (Exemplo:  .).')
    tara_balanca = models.ForeignKey(TaraBalanca,on_delete=False, verbose_name="Tara da Balança",
                            help_text='Tara da Balança (Exemplo: .).')
    tecla  = models.CharField(max_length=200, verbose_name="Tecla",
                                help_text='Tecla (Exemplo:.).')
    status = models.ForeignKey(Status,on_delete=False, verbose_name="Status",
                            help_text='Status (Exemplo: .).')
    tipo_venda = models.ForeignKey(TipoVenda,on_delete=False, verbose_name="Tipo Venda",
                            help_text='Tipo Venda (Exemplo: Leite, Ovo , etc .).')
    q_e_compra = models.PositiveIntegerField( verbose_name="Q. E. Compra",
                            help_text='Q. E. Compra (Exemplo:.).')
    embalagem_compra = models.ForeignKey(EmbalagemCompra,on_delete=False, verbose_name="Embalagem de Compra",
                            help_text='Embalagem de Compra (Exemplo: .).')
    imagem = models.FileField(upload_to='media/produto/', verbose_name="Imagem",
                            help_text='Imagem (Exemplo:  .).')
    comissao = models.ForeignKey(Comissao,on_delete=False, verbose_name="Comissão",
                            help_text='Comissão (Exemplo: .).')
    garantia = models.ForeignKey(Garantia,on_delete=False, verbose_name="Garantia",
                            help_text='Garantia (Exemplo:  .).')
    codigo_vasilhame = models.ForeignKey(Vasilhame,on_delete=False, verbose_name="Código do Vasilhame",
                            help_text='Código vasilhame (Exemplo:  .).')
    categoria_ecomerce = models.ForeignKey(CategoriaEComerce,on_delete=False, verbose_name="Categoria E-Cormece",
                            help_text='Categoria E-Comerce (Exemplo: .)')
    cest = models.ForeignKey(Cest, on_delete=False,verbose_name="CEST",
                            help_text='CEST (Exemplo: Leite, Ovo , etc .).')
    anp = models.ForeignKey(Anp,on_delete=False, verbose_name="ANP",
                            help_text='ANP(Exemplo: Leite, Ovo , etc .).')
    item = models.ManyToManyField(Item, verbose_name="Itens Extras",
                            help_text='Itens Extras(Exemplo: Leite, Ovo , etc .).')
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
