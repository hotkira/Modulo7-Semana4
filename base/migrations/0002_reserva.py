# Generated by Django 4.2.1 on 2023-07-13 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeDoPet', models.CharField(max_length=50)),
                ('telefone', models.CharField(max_length=15)),
                ('dia', models.DateField()),
                ('observacoes', models.TextField()),
                ('data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]