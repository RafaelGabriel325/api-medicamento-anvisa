# Generated by Django 5.1.1 on 2024-09-25 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicacao',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('substancia', models.CharField(max_length=255)),
                ('cnpj', models.CharField(max_length=255)),
                ('laboratorio', models.CharField(max_length=255)),
                ('codigo_ggrem', models.CharField(max_length=255)),
                ('registro', models.CharField(max_length=255)),
                ('ean_1', models.CharField(max_length=255)),
                ('ean_2', models.CharField(blank=True, max_length=255, null=True)),
                ('produto', models.CharField(max_length=255)),
                ('apresentacao', models.CharField(max_length=255)),
                ('classe_terapeutica', models.CharField(max_length=255)),
                ('tipo_produto', models.CharField(max_length=255)),
                ('regime_preco', models.CharField(max_length=255)),
                ('pf_sem_impostos', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('pf_0', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('pf_12', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('pf_12_alc', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('pf_17', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('pf_17_alc', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('pf_17_5', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('pf_17_5_alc', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('pf_18', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('pf_18_alc', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('pf_19', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('pf_19_alc', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('pf_19_5', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('pf_19_5_alc', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('pf_20', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('pf_20_alc', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('pf_20_5', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('pf_21', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('pf_21_alc', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('pf_22', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('pf_22_alc', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('pmc_sem_imposto', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('pmc_0', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('pmc_12', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('pmc_12_alc', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('pmc_17', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('pmc_17_alc', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('pmc_17_5', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('pmc_17_5_alc', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('pmc_18', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('pmc_18_alc', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('pmc_19', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('pmc_19_alc', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('pmc_19_5', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('pmc_19_5_alc', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('pmc_20', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('pmc_20_alc', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('pmc_20_5', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('pmc_21', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('pmc_21_alc', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('pmc_22', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('pmc_22_alc', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('restricao_hospitalar', models.CharField(max_length=255)),
                ('cap', models.CharField(max_length=255)),
                ('confaz_87', models.CharField(max_length=255)),
                ('icms_0', models.CharField(max_length=255)),
                ('analise_recursal', models.CharField(blank=True, max_length=255, null=True)),
                ('lista_concessao_credito', models.CharField(max_length=255)),
                ('comercializacao_2022', models.CharField(max_length=255)),
                ('tarja', models.CharField(blank=True, max_length=255, null=True)),
                ('destinacao_comercial', models.CharField(max_length=255)),
            ],
        ),
    ]
