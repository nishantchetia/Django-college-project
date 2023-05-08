from django.db import models


class HydraulicCompany(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class HydraulicProduct(models.Model):
    company = models.ForeignKey(HydraulicCompany, on_delete=models.CASCADE, related_name='company')
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Industrial_Company(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Industrial_Product(models.Model):
    company = models.ForeignKey(Industrial_Company, on_delete=models.CASCADE, related_name='ind_company')
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class MCW_Company(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class MCW_Product(models.Model):
    company = models.ForeignKey(MCW_Company, on_delete=models.CASCADE, related_name='mcw_company')
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class RCO_Company(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class RCO_Product(models.Model):
    company = models.ForeignKey(RCO_Company, on_delete=models.CASCADE, related_name='rco_company')
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class SPL_Company(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class SPL_Product(models.Model):
    company = models.ForeignKey(SPL_Company, on_delete=models.CASCADE, related_name='spl_company')
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class TRS_Company(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class TRSProduct(models.Model):
    company = models.ForeignKey(TRS_Company, on_delete=models.CASCADE, related_name='trs_company')
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class TUR_Company(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class TUR_Product(models.Model):
    company = models.ForeignKey(TUR_Company, on_delete=models.CASCADE, related_name='tur_company')
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class WIRCompany(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class WIRProduct(models.Model):
    company = models.ForeignKey(WIRCompany, on_delete=models.CASCADE, related_name='wir_company')
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class IN_GreaseCompany(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class IN_GreaseProduct(models.Model):
    company = models.ForeignKey(IN_GreaseCompany, on_delete=models.CASCADE, related_name='ing_company')
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class AO_Company(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class AO_Product(models.Model):
    company = models.ForeignKey(AO_Company, on_delete=models.CASCADE, related_name='ao_company')
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class AGO_Company(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class AGO_Product(models.Model):
    company = models.ForeignKey(AGO_Company, on_delete=models.CASCADE, related_name='ago_company')
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class RDC_Company(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class RDC_Product(models.Model):
    company = models.ForeignKey(RDC_Company, on_delete=models.CASCADE, related_name='rdc_company')
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
