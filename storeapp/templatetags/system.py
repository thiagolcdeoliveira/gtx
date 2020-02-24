import datetime

from django import template

from storeapp.models.chamado import Chamado

register = template.Library()

# @register.filter(name='chamadosmes')
@register.simple_tag(name='chamadosmesaberto')
def chamadosmesaberto():
    data = datetime.datetime.now()

    data = (data.strftime("%Y-%m-01 00:00:00"))

   # date = datetime.strptime(d, '%b %d %Y %I:%M%p')
    # if data.mouth == '12':
    #     soma= 1
    # else:
    #     soma  = 0
    # x = datetime.datetime(data.year + soma, data.mouth + 1 %12, 00)
    # data_fim datetime.timedelta(mouth=1)
    # d = d + relativedelta(months=1)
    # print(data)
    chamados =  Chamado.objects.filter(excluido=False, desativado=False, data_inicio__gte=data,status=False)
    # chamados ={'chamadosaberto': len(chamados.filter(status=False)), 'chamadosfechado': len(chamados.filter(status=True)) }
    return len(chamados)

@register.filter(name='chamadosano')
def chamdosano(user):
    chamados = Chamado.objects.filter(excluido=False, desativado=False)
    chamados = Chamado.objects.filter(excluido=False, desativado=False, data_inicio__gte=data, status=False)
    # chamados ={'chamadosaberto': len(chamados.filter(status=False)), 'chamadosfechado': len(chamados.filter(status=True)) }
    return len(chamados)
@register.filter(name='chamadosaberto')
def chamadosaberto(id):
    pedido = Pedido.objects.get(id=id)


    chamados = Chamado.objects.filter(excluido=False, desativado=False, data_inicio__gte=data, status=False)
    # chamados ={'chamadosaberto': len(chamados.filter(status=False)), 'chamadosfechado': len(chamados.filter(status=True)) }
    return len(chamados)


@register.filter(name='chamadospessoais')
def chamadospessoais(id):
    chamados = Chamado.objects.filter(excluido=False, desativado=False, responsavel_username=id, status=False)
    # chamados ={'chamadosaberto': len(chamados.filter(status=False)), 'chamadosfechado': len(chamados.filter(status=True)) }
    return len(chamados)

@register.filter(name='produtos')
def produtos(id):
    pedido = Pedido.objects.get(id=id)
    return pedido.preco_unit > pedido.produto.preco_unit
