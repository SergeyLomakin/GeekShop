# Generated by Django 3.1 on 2021-06-19 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0003_auto_20210619_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='age',
            field=models.PositiveIntegerField(verbose_name='возраст'),
        ),
    ]