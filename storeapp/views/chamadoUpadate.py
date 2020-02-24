# coding=utf-8
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import *

from storeapp.forms.chamado import ChamadoForm, ChamadoUpdateForm
from storeapp.models.chamado import Chamado
from storeapp.models.produto import Produto
from storeapp.forms.produto import ProdutoForm
from storeapp.variaveis import *


# class TipoArquivoCreateView(PermissionRequiredMixin, CreateView):
class ChamadoUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ADD_CHAMADO
    template_name = 'chamado/chamado_form.html'
    model = Chamado
    form_class = ChamadoUpdateForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.usuario = self.request.user
        self.object.save()
        return super(ChamadoUpdateView, self).form_valid(form)
