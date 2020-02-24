# coding=utf-8
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import *
from storeapp.models.produto import Produto
from storeapp.forms.produto import ProdutoForm
from storeapp.variaveis import *


# class TipoArquivoCreateView(PermissionRequiredMixin, CreateView):
class ProdutoDetail(PermissionRequiredMixin, DetailView):
    permission_required = ADD_PRODUTO
    template_name = 'produto/produto_detail.html'
    model = Produto


    # form_class = ProdutoForm

    # def form_valid(self, form):
    #     self.object = form.save(commit=False)
    #     self.object.usuario = self.request.user
    #     self.object.save()
    #     return super(ProdutoCreateView, self).form_valid(form)

    # def get_queryset(self):
         #return self.queryset.get_object_or_404(pk=self.kwargs['id'])
         #return get_object_or_404(self.queryset,pk=self.kwargs['id'])
         # return get_object_or_404(Produto,pk=self.kwargs['id'])
         # return get_object_or_404(Produto,pk=self.kwargs['id'])
         # return get_object_or_404(Produto,pk=self.kwargs['pk'])