# Generated by Django 4.1.1 on 2022-10-10 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportajes', '0011_usuarios_contrasena'),
    ]

    operations = [
        migrations.AddField(
            model_name='camarografo',
            name='contrasena',
            field=models.CharField(default=str, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reporteross',
            name='contrasena',
            field=models.CharField(default=str, max_length=50),
            preserve_default=False,
        ),
    ]