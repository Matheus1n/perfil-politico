# Generated by Django 3.2.5 on 2021-10-08 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_django_3_2_update_use_big_auto_field_for_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='affiliation',
            name='electoral_section',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='affiliation',
            name='status',
            field=models.CharField(choices=[('R', 'Regular'), ('C', 'Cancelado'), ('D', 'Desfiliado'), ('S', 'Sub judice'), ('T', 'Transferido')], max_length=1),
        ),
        migrations.AlterField(
            model_name='asset',
            name='detail',
            field=models.CharField(blank=True, default='', max_length=400),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='state',
            field=models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins'), ('ND', 'Não Divulgável'), ('BR', 'Nacional'), ('VT', 'Voto em trânsito'), ('ZZ', 'Exterior')], max_length=2),
        ),
        migrations.AlterField(
            model_name='city',
            name='state',
            field=models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins'), ('ND', 'Não Divulgável'), ('BR', 'Nacional'), ('VT', 'Voto em trânsito'), ('ZZ', 'Exterior')], max_length=2),
        ),
    ]
