# Generated by Django 2.2.6 on 2020-01-22 12:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome da Categoria (Exemplo: .).', max_length=200, verbose_name='Nome da Categoria')),
                ('descricao', models.CharField(help_text='Descrição (Exemplo: .).', max_length=200, verbose_name='Descrição')),
                ('quantidade', models.PositiveIntegerField(help_text='Quantidade (Exemplo: .).', verbose_name='Quantidade')),
                ('principal', models.CharField(help_text='Principal (Exemplo: .).', max_length=200, verbose_name='Principal')),
                ('unidade', models.CharField(help_text='Unidade (Exemplo: .).', max_length=200, verbose_name='Unidade')),
                ('secundaria', models.CharField(help_text='Secundária (Exemplo:  .).', max_length=200, verbose_name='Secundária')),
                ('fabricante', models.CharField(help_text='Nome do Fabricante (Exemplo: Leite, Ovo , etc .).', max_length=200, verbose_name='Nome do Fabricante')),
                ('secao', models.CharField(help_text='Seção/Categoria (Exemplo: Leite, Ovo , etc .).', max_length=200, verbose_name='Seção/Categoria')),
                ('grupo', models.CharField(help_text='Grupo (Exemplo:  .).', max_length=200, verbose_name='Gruṕo')),
                ('grade_produto', models.CharField(help_text='Grade de Produtos (Exemplo:  .).', max_length=200, verbose_name='Grade de Produtos')),
                ('excluido', models.BooleanField(default=False, verbose_name='Excluído')),
                ('desativado', models.BooleanField(default=False)),
                ('usuario', models.ForeignKey(on_delete=False, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Produto',
                'permissions': (('store_add_produto', 'Adicionar Produto'), ('store_detail_produto', 'Visualizar Produto')),
                'verbose_name_plural': 'Produtos',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome do Produto (Exemplo: Leite, Ovo , etc .).', max_length=200, verbose_name='Nome do Produto')),
                ('excluido', models.BooleanField(default=False, verbose_name='Excluído')),
                ('desativado', models.BooleanField(default=False)),
                ('usuario', models.ForeignKey(on_delete=False, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Item',
                'permissions': (('store_add_produto', 'Adicionar Produto'), ('store_detail_produto', 'Visualizar Produto')),
                'verbose_name_plural': 'Itens',
            },
        ),
        migrations.CreateModel(
            name='TipoProduto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Tipo de Produto', max_length=200, verbose_name='Tipo Produto')),
                ('excluido', models.BooleanField(default=False, verbose_name='Excluído')),
                ('desativado', models.BooleanField(default=False)),
                ('usuario', models.ForeignKey(on_delete=False, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Tipo de Produto',
                'permissions': (('store_add_produto', 'Adicionar Produto'), ('store_detail_produto', 'Visualizar Produto')),
                'verbose_name_plural': 'Tipos de Produtos',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Descrição.', max_length=200, verbose_name='Descrição')),
                ('excluido', models.BooleanField(default=False, verbose_name='Excluído')),
                ('desativado', models.BooleanField(default=False)),
                ('usuario', models.ForeignKey(on_delete=False, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Satus',
                'permissions': (('store_add_produto', 'Adicionar Produto'), ('store_detail_produto', 'Visualizar Produto')),
                'verbose_name_plural': 'Status',
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome do Produto (Exemplo: Leite, Ovo , etc .).', max_length=200, verbose_name='Nome do Produto')),
                ('codigo_barras', models.CharField(help_text='Código de Barras (Exemplo: 000001).', max_length=200, verbose_name='Código de Barras')),
                ('complemento_nome', models.CharField(help_text='Complemento do Nome (Exemplo: Não sei).', max_length=200, verbose_name='Complemento do Nome')),
                ('imagem', models.FileField(blank=True, help_text='Imagem (Exemplo:  .).', upload_to='media/produto/', verbose_name='Imagem')),
                ('excluido', models.BooleanField(default=False, verbose_name='Excluído')),
                ('desativado', models.BooleanField(default=False)),
                ('categoria', models.ForeignKey(blank=True, help_text='Complemento do Nome (Exemplo: Não sei).', null=True, on_delete=False, to='storeapp.Categoria', verbose_name='Complemento do Nome')),
                ('item', models.ManyToManyField(help_text='Itens Extras(Exemplo: Leite, Ovo , etc .).', to='storeapp.Item', verbose_name='Itens Extras')),
                ('status', models.ForeignKey(help_text='Status (Exemplo: .).', on_delete=False, to='storeapp.Status', verbose_name='Status')),
                ('tipo_produto', models.ForeignKey(help_text='Tipo de Produto: Selecione um tipo de produto (Exemplo: Estoque).', on_delete=False, to='storeapp.TipoProduto', verbose_name='Tipo de Produto.')),
                ('usuario', models.ForeignKey(on_delete=False, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Produto',
                'permissions': (('store_add_produto', 'Adicionar Produto'), ('store_detail_produto', 'Visualizar Produto')),
                'verbose_name_plural': 'Produtos',
            },
        ),
        migrations.CreateModel(
            name='Imagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.CharField(help_text='Nome do Produto (Exemplo: Leite, Ovo , etc .).', max_length=200, verbose_name='Nome do Produto')),
                ('excluido', models.BooleanField(default=False, verbose_name='Excluído')),
                ('desativado', models.BooleanField(default=False)),
                ('usuario', models.ForeignKey(on_delete=False, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Imagem',
                'permissions': (('store_add_imagem', 'Adicionar imagem'), ('store_detail_imagens', 'Visualizar imagem')),
                'verbose_name_plural': 'Imagens',
            },
        ),
        migrations.CreateModel(
            name='Chamado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod', models.CharField(max_length=200, unique=True, verbose_name='Codigo do Chamado')),
                ('descricao', models.TextField(help_text='Nome do Produto (Exemplo: Leite, Ovo , etc .).', max_length=200, verbose_name='Nome do Produto')),
                ('excluido', models.BooleanField(default=False, verbose_name='Excluído')),
                ('desativado', models.BooleanField(default=False)),
                ('funcionario', models.ForeignKey(help_text='Funcionario que está solicitando o conserto.', on_delete=False, related_name='funcionario_usuario', to=settings.AUTH_USER_MODEL, verbose_name='Funcionario')),
                ('imagem', models.ManyToManyField(blank=True, to='storeapp.Imagem')),
                ('produto_utilizado', models.ManyToManyField(blank=True, to='storeapp.Produto')),
                ('responsavel', models.ForeignKey(help_text='Funcionario responsavel pelo conserto.', on_delete=False, related_name='responsavel_usuario', to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
                ('usuario', models.ForeignKey(on_delete=False, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Chamado',
                'permissions': (('store_add_chamado', 'Adicionar chamado'), ('store_detail_chamado', 'Visualizar chamado')),
                'verbose_name_plural': 'Chamados',
            },
        ),
    ]
