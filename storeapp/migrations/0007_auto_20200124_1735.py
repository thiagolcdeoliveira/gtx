# Generated by Django 2.2.6 on 2020-01-24 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0006_chamado_data_inicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chamado',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
