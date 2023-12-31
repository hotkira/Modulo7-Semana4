# Generated by Django 4.2.1 on 2023-07-19 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_reserva'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contato',
            options={'ordering': ['-data'], 'verbose_name': 'Formulário de Contato', 'verbose_name_plural': 'Formulários de Contatos'},
        ),
        migrations.AddField(
            model_name='contato',
            name='lido',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
