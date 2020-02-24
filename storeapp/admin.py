from django.contrib import admin

from storeapp.models.categoria import Categoria
from storeapp.models.chamado import Chamado
from storeapp.models.imagem import Imagem
from storeapp.models.item import Item
from storeapp.models.produto import Produto
# Register your models here.
from storeapp.models.status import Status
from storeapp.models.tipo_produto import TipoProduto

admin.site.register(Produto)
admin.site.register(Imagem)
admin.site.register(Chamado)
admin.site.register(TipoProduto)
admin.site.register(Status)
admin.site.register(Item)
admin.site.register(Categoria)
