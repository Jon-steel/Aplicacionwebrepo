# Generated by Django 4.1.1 on 2022-09-14 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportajes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reportajes',
            name='id',
        ),
        migrations.AlterField(
            model_name='reportajes',
            name='disco',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
