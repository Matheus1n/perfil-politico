# Generated by Django 2.1 on 2018-08-27 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mandate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='politician',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tweets', to='mandate.Politician'),
        ),
    ]
