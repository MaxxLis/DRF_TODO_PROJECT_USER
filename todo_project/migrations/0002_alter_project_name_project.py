# Generated by Django 4.0.4 on 2022-05-25 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='name_project',
            field=models.CharField(max_length=128, unique=True, verbose_name='Название проекта'),
        ),
    ]