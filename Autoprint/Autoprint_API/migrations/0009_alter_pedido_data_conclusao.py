# Generated by Django 4.2.3 on 2023-10-07 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Autoprint_API', '0008_alter_pedido_id_agent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='data_conclusao',
            field=models.DateField(default=None, null=True),
        ),
    ]
