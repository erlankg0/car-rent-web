# Generated by Django 3.2.7 on 2021-09-11 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_auto_20210911_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
