# Generated by Django 4.2.1 on 2023-08-16 22:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0004_petshop_reserva_petshop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='petshop',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reserva', to='reserva.petshop'),
        ),
    ]