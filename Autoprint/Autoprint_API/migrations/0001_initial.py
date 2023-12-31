# Generated by Django 4.2.3 on 2023-10-03 20:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=500)),
                ('token', models.CharField(max_length=512)),
                ('foto', models.CharField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('categoria', models.CharField(max_length=50)),
                ('foto', models.CharField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Impressora',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('marca', models.CharField(max_length=100)),
                ('modelo', models.CharField(max_length=200)),
                ('localizacao', models.CharField(max_length=800)),
                ('foto', models.CharField()),
                ('id_agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Autoprint_API.agente')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('idConf_inpre', models.IntegerField()),
                ('idConf_cli', models.IntegerField()),
                ('data_pedido', models.DateField()),
                ('data_conclusao', models.DateField()),
                ('id_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Autoprint_API.cliente')),
                ('id_impressora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Autoprint_API.impressora')),
            ],
        ),
        migrations.CreateModel(
            name='Impressao',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('documento', models.CharField()),
                ('data_criacao', models.DateField()),
                ('pedido', models.IntegerField()),
                ('id_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Autoprint_API.cliente')),
            ],
        ),
    ]
