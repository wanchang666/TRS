# Generated by Django 2.0 on 2018-01-24 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Photo', '0005_auto_20180124_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='title',
            field=models.TextField(null=True),
        ),
    ]
