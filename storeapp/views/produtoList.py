# coding=utf-8
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import *

from storeapp.forms.chamado import ChamadoForm
from storeapp.models.chamado import Chamado
from storeapp.models.produto import Produto
from storeapp.forms.produto import ProdutoForm
from storeapp.variaveis import *


# class TipoArquivoCreateView(PermissionRequiredMixin, CreateView):
class ProdutoListView(PermissionRequiredMixin, ListView):
    permission_required = ADD_CHAMADO
    template_name = 'chamado/chamado_list.html'
    model = Produto
    queryset = Produto
    paginate_by = 10
    # form_class = ChamadoForm

    # def form_valid(self, form):
    #     self.object = form.save(commit=False)
    #     self.object.usuario = self.request.user
    #     self.object.save()
    #     return super(ChamadoCreateView, self).form_valid(form)
    def get_queryset(self):


        # print(self.kwargs.get())
        # descricao = self.request.GET.get("tipo")
        # descricao = self.request.GET
        form = self.request.GET
        if form.get('tipo'):
            if form.get('tipo') == 1:
                self.queryset = self.queryset.objects.filter(nome__contains=form.get('descricao'))
            elif form.get('tipo') == 2:
                self.queryset = self.queryset.objects.filter(patrimonio__contains=form.get('descricao'))
            # elif form.get('tipo') == 3:
            #     self.queryset = self.queryset.objects.filter(responsavel_username__contains=form.get('descricao'))
        if form.get('status'):
            self.queryset = self.queryset.objects.filter(status_pk=form.get('status'))
        if form.get('data_inicio'):
            self.queryset = self.queryset.objects.filter(data_incio__lte=form.get('data_inicio'))
        if form.get('data_fim'):
            self.queryset = self.queryset.objects.filter(data_fim__gte=form.get('data_fim'))
        # if form.get('tipo'):

        # form_key = self.request.GET.key

        # print(descricao)
        # queryset = self.queryset.objects.filter(descricao__contains='')

        return self.queryset.objects.filter(excluido=False)