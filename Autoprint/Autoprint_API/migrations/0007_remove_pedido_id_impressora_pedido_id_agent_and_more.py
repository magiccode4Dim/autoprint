# Generated by Django 4.2.3 on 2023-10-07 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Autoprint_API', '0006_alter_impressao_pedido'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='id_impressora',
        ),
        migrations.AddField(
            model_name='pedido',
            name='id_agent',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Autoprint_API.agente'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='isconfirmed',
            field=models.BooleanField(default=False),
        ),
    ]