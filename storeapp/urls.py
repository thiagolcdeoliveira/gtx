# coding=utf-8
from __future__ import unicode_literals
from django.conf.urls import url

from storeapp.views.chamadoAbrir import ChamadoAbrirView
from storeapp.views.chamadoCreate import ChamadoCreateView
from storeapp.views.chamadoDetail import ChamadoDetailView
from storeapp.views.chamadoFechar import ChamadoFecharView
from storeapp.views.chamadoList import ChamadoListView
from storeapp.views.chamadoUpadate import ChamadoUpdateView
from storeapp.views.home import HomeView
from storeapp.views.produtoCreate import ProdutoCreateView
from storeapp.views.produtoDetail import ProdutoDetail
from storeapp.views.produtoList import ProdutoListView

urlpatterns = [

    # ---- Produto ----#
    url(r'^produto/cadastrar/$', ProdutoCreateView.as_view(),
        name='produto-add'),
    #url(r'^produto/vizualizar/(?P<id>[\d\-]+)/$', ProdutoDetail.as_view(),
    url(r'^produto/vizualizar/(?P<pk>[\d\-]+)/$', ProdutoDetail.as_view(),
        name='produto-detail'),
    url(r'^produto/listar/$', ProdutoListView.as_view(),
        name='produto-list'),

    url(r'^chamado/cadastrar$', ChamadoCreateView.as_view(),
        name='chamado-add'),
    url(r'^chamado/listar$', ChamadoListView.as_view(),
        name='chamado-list'),
    url(r'^chamado/vizualizar/(?P<pk>[\d\-]+)/$', ChamadoDetailView.as_view(),
        name='chamado-detail'),
    url(r'^chamado/atualizar/(?P<pk>[\d\-]+)/$', ChamadoUpdateView.as_view(),
        name='chamado-update'),
    url(r'^chamado/excluir/(?P<pk>[\d\-]+)/$', ChamadoCreateView.as_view(),
        name='chamado-delete'),
    url(r'^chamado/fechar/(?P<pk>[\d\-]+)', ChamadoFecharView.as_view(),
        name='chamado-fechar'),
    url(r'^chamado/abrir/(?P<pk>[\d\-]+)', ChamadoAbrirView.as_view(),
        name='chamado-abrir'),

    url(r'^p/$', HomeView.as_view(),
        name='home'),
    url(r'^/$', HomeView.as_view(),
        name='home'),
    url(r'^$', HomeView.as_view(),
        name='home'),

]