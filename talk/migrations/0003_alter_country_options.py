# Generated by Django 4.2.6 on 2023-10-20 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('talk', '0002_alter_country_name_alter_producter_country_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name': 'Страна'},
        ),
    ]