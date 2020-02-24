# coding=utf-8
from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import *

from storeapp.forms.chamado import ChamadoForm
from storeapp.models.chamado import Chamado
from storeapp.models.produto import Produto
from storeapp.forms.produto import ProdutoForm
from storeapp.variaveis import *
from django.utils.translation import ugettext_lazy as _

# class TipoArquivoCreateView(PermissionRequiredMixin, CreateView):
class ChamadoFechar1View(PermissionRequiredMixin, DeleteView):
    permission_required = ADD_CHAMADO
    template_name = 'chamado/chamado_list.html'
    model = Chamado
    # form_class = ChamadoForm
    #
    # def form_valid(self, form):
    #     self.object = form.save(commit=False)
    #     self.object.usuario = self.request.user
    #     self.object.save()
    #     return super(ChamadoCreateView, self).form_valid(form)
    success_message = _("Chamado Fechado com sucesso!")

    queryset = Chamado.objects.all()
    success_url = reverse_lazy('chamado-list')

    # def form_valid(self, form):
    #     self.object = form.save(commit=False)
    #     self.object.status = True
    #     self.object.save()
    #     messages.success(self.request, self.success_message)
    #
    #     return super(ChamadoFecharView, self).form_valid(form)

    # def save(self, commit=True):
    #     self.object = form.save(commit=False)
    #     self.object.status = True
    #     self.object.save()
    #     messages.success(self.request, self.success_message)
    #     return self.object
    #
    # def get(self, *args, **kwargs):
    #     return self.post(*args, **kwargs)

    def delete(self, request, *args, **kwargs):

        self.object = self.get_object()
            # form.save(commit=False)
        self.object.status = True
        self.object.save()
        # messages.success(self.request, self.success_message)
        # return  HttpResponseRedirect(self.success_url)
        return  HttpResponseRedirect(self.success_url)



    #     return super(ChamadoFecharView, self).form_valid(form)
    # def post(self, request, *args, **kwargs):
    #
    #     return reverse_lazy('chamado-list')

class ChamadoFecharView(View):

        def get(self,request,**kwargs):
            chamado= get_object_or_404(Chamado,pk=self.kwargs['pk'])
            chamado.status = True
            chamado.save()
            return HttpResponseRedirect(reverse_lazy('chamado-list'))
