# Generated by Django 5.1.5 on 2025-01-23 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='genre',
        ),
        migrations.AlterField(
            model_name='author',
            name='surname',
            field=models.CharField(blank=True, max_length=200, verbose_name='Отчество'),
        ),
    ]