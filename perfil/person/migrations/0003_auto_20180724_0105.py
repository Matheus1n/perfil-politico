# Generated by Django 2.0.7 on 2018-07-24 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0002_auto_20180723_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='birthdate',
            field=models.DateField(max_length=250, null=True),
        ),
    ]
