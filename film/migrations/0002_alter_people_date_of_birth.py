# Generated by Django 4.0.4 on 2022-05-30 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='date_of_birth',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Дата рождения'),
        ),
    ]