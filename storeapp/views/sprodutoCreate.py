# coding=utf-8
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import *
from storeapp.models.produto import Produto
from storeapp.forms.produto import ProdutoForm
from storeapp.variaveis import *


# class TipoArquivoCreateView(PermissionRequiredMixin, CreateView):
class ProdutoCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ADD_PRODUTO
    template_name = 'produto/produto_form.html'
    model = Produto
    form_class = ProdutoForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.usuario = self.request.user
        self.object.save()
        return super(ProdutoCreateView, self).form_valid(form)
