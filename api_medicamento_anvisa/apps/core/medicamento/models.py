from django.db import models


class Medicacao(models.Model):
    id = models.AutoField(primary_key=True)
    substancia = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=255)
    laboratorio = models.CharField(max_length=255)
    codigo_ggrem = models.CharField(max_length=255)
    registro = models.CharField(max_length=255)
    ean_1 = models.CharField(max_length=255)
    ean_2 = models.CharField(max_length=255, blank=True, null=True)
    produto = models.CharField(max_length=255)
    apresentacao = models.CharField(max_length=255)
    classe_terapeutica = models.CharField(max_length=255)
    tipo_produto = models.CharField(max_length=255)
    regime_preco = models.CharField(max_length=255)
    pf_sem_impostos = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pf_0 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pf_12 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pf_12_alc = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pf_17 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pf_17_alc = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pf_17_5 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pf_17_5_alc = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pf_18 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pf_18_alc = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pf_19 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pf_19_alc = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pf_19_5 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pf_19_5_alc = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pf_20 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pf_20_alc = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pf_20_5 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pf_21 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pf_21_alc = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pf_22 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pf_22_alc = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pmc_sem_imposto = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pmc_0 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pmc_12 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pmc_12_alc = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pmc_17 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pmc_17_alc = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pmc_17_5 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pmc_17_5_alc = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pmc_18 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pmc_18_alc = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pmc_19 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pmc_19_alc = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pmc_19_5 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pmc_19_5_alc = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pmc_20 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pmc_20_alc = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pmc_20_5 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pmc_21 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pmc_21_alc = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pmc_22 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pmc_22_alc = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    restricao_hospitalar = models.CharField(max_length=255)
    cap = models.CharField(max_length=255)
    confaz_87 = models.CharField(max_length=255)
    icms_0 = models.CharField(max_length=255)
    analise_recursal = models.CharField(max_length=255, null=True, blank=True)
    lista_concessao_credito = models.CharField(max_length=255)
    comercializacao_2022 = models.CharField(max_length=255)
    tarja = models.CharField(max_length=255, null=True, blank=True)
    destinacao_comercial = models.CharField(max_length=255)
