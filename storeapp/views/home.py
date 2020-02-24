# coding=utf-8
import datetime

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import *

from storeapp.forms.chamado import ChamadoForm
from storeapp.models.chamado import Chamado
from storeapp.models.produto import Produto
from storeapp.forms.produto import ProdutoForm
from storeapp.variaveis import *


# class TipoArquivoCreateView(PermissionRequiredMixin, CreateView):
class HomeView(PermissionRequiredMixin, CreateView):
    permission_required = ADD_CHAMADO
    # template_name = 'home.html'
    template_name = 'home_dashboard.html'
    # template_name = 'home.html'
    model = Chamado
    form_class = ChamadoForm

    # def get_context_data(self, **kwargs):
    #     return

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data1 = datetime.datetime.now()

        data = (data1.strftime("%Y-%m-01 00:00:00"))
        data_ano = (data1.strftime("%Y-01-01 00:00:00"))
        chamado = Chamado.objects.filter(excluido=False, desativado=False,)
        chamadosmesaberto = chamado.filter(data_inicio__gte=data, status=False)
        chamadosmesfechado = chamado.filter(data_inicio__gte=data, status=True)
        chamadosanoaberto = chamado.filter(data_inicio__gte=data_ano, status=False)
        chamadosanofechado = chamado.filter(data_inicio__gte=data_ano, status=True)

        context['chamadosmes'] = {'chamadoaberto': len(chamadosmesaberto), 'chamadofechado': len(chamadosmesfechado)}
        context['chamadosano'] = {'chamadoaberto': len(chamadosanoaberto), 'chamadofechado': len(chamadosanofechado)}

        return context
    # def form_valid(self, form):
    #     self.object = form.save(commit=False)
    #     self.object.usuario = self.request.user
    #     self.object.save()
    #     return super(ChamadoCreateView, self).form_valid(form)
# class TipoArquivoCreateView(PermissionRequiredMixin, CreateView):
# class HomeView(PermissionRequiredMixin, CreateView):
#     permission_required = ADD_CHAMADO
#     # template_name = 'home.html'
#     template_name = 'home_dashboard.html'
#     # template_name = 'home.html'
#     model = Chamado
#     form_class = ChamadoForm
#
#     # def form_valid(self, form):
    #     self.object = form.save(commit=False)
    #     self.object.usuario = self.request.user
    #     self.object.save()
    #     return super(ChamadoCreateView, self).form_valid(form)
