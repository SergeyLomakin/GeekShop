# Generated by Django 3.1 on 2021-06-21 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0004_auto_20210619_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='age',
            field=models.PositiveIntegerField(blank=True, verbose_name='возраст'),
        ),
    ]
