# Generated by Django 2.0.7 on 2018-07-25 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mandate', '0001_initial'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='activity',
            index=models.Index(fields=['position'], name='mandate_act_positio_074715_idx'),
        ),
        migrations.AddIndex(
            model_name='politic',
            index=models.Index(fields=['congressperson_id'], name='mandate_pol_congres_f69287_idx'),
        ),
        migrations.AddIndex(
            model_name='politic',
            index=models.Index(fields=['congressperson_name'], name='mandate_pol_congres_d48e69_idx'),
        ),
        migrations.AddIndex(
            model_name='term',
            index=models.Index(fields=['position'], name='mandate_ter_positio_4453b7_idx'),
        ),
    ]
