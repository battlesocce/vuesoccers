# Generated by Django 2.1.7 on 2020-08-25 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200817_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='highlights',
            name='highlight',
            field=models.URLField(),
        ),
    ]