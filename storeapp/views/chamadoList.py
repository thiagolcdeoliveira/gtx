# coding=utf-8
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import *

from storeapp.forms.chamado import ChamadoForm
from storeapp.models.chamado import Chamado
from storeapp.models.produto import Produto
from storeapp.forms.produto import ProdutoForm
from storeapp.variaveis import *


# class TipoArquivoCreateView(PermissionRequiredMixin, CreateView):
class ChamadoListView(PermissionRequiredMixin, ListView):
    permission_required = ADD_CHAMADO
    template_name = 'chamado/chamado_list.html'
    model = Chamado
    queryset = Chamado
    paginate_by = 10
    # form_class = ChamadoForm

    # def form_valid(self, form):
    #     self.object = form.save(commit=False)
    #     self.object.usuario = self.request.user
    #     self.object.save()
    #     return super(ChamadoCreateView, self).form_valid(form)
    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super(ChamadoListView, self).get_context_data(**kwargs)
    #     context['dahl_books'] = Chamado.objects.filter(descricao__contains='')
    #     print(kwargs.get('tipo'))
    #     return  context

    def get_queryset(self):
         # print(self.kwargs.get())
         # descricao = self.request.GET.get("tipo")
         # descricao = self.request.GET
         form = self.request.GET
         self.queryset = Chamado.objects.all()
         if form.get('tipo'):
             if form.get('tipo') == '1':
                self.queryset = self.queryset.filter(descricao__contains=form.get('descricao'))
             elif form.get('tipo') == '2':
                 self.queryset = self.queryset.filter(funcionario__username__contains=form.get('descricao'))
             elif form.get('tipo') == '4':
                 print(form.get('tipo'))
                 print(form.get('descricao'))
                 self.queryset = self.queryset.filter(pk=form.get('descricao'))
             elif form.get('tipo') == '3':
                 self.queryset = self.queryset.filter(responsavel__username__contains=form.get('descricao'))
         if form.get('status')=='1':
             self.queryset = self.queryset.filter(status=False)
         elif form.get('status')=='2':
             self.queryset = self.queryset.filter(status=True)
         print(form.get('data_incio'))
         print(form)
         if form.get('data_incio'):
             self.queryset = self.queryset.filter(data_inicio__gte=form.get('data_incio'))
         if form.get('data_fim'):
             self.queryset = self.queryset.filter(data_inicio__lte=form.get('data_fim'))
         if form.get('data_incio_encerramento'):
             self.queryset = self.queryset.filter(data_fim__gte=form.get('data_incio_encerramento'))
         if form.get('data_fim_encerramento'):
             self.queryset = self.queryset.filter(data_fim__lte=form.get('data_fim_encerramento'))
         # if form.get('tipo'):

         # form_key = self.request.GET.key

         # print(descricao)
         # queryset = self.queryset.objects.filter(descricao__contains='')

         return self.queryset.filter(excluido=False)