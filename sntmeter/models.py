from django.db import models
from simple_history.models import HistoricalRecords
from .validators import validar_metodo, validar_nombre
# Aqui los modelos del software de lectura de medidores

class Vendor(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, validators=[validar_nombre])
    
    def __str__(self):
        return self.name

class Model(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null = True)
    def __str__(self):
        return self.name
    
class Con_method(models.Model):
    type = models.CharField(max_length=20, null=False,blank=False, validators=[validar_metodo])
    def __str__(self):
        return self.type
    
class Meter(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    serial = models.CharField(max_length=50, null=False, blank=False, default='NoS/N')
    logical_name = models.CharField(max_length=50, null=True, blank=True)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    location = models.CharField(max_length=50, null=True, blank=True)
    group = models.CharField(max_length=50, null=True, blank=True)
    con_method = models.ForeignKey(Con_method, on_delete=models.CASCADE,null=True, blank=True)
    con_port = models.CharField(max_length=30, null=True, blank=True)
    con_ip = models.GenericIPAddressField(null=True,blank=True)
    baud_rate = models.IntegerField(null=True,blank=True, default=9600)
    pot_act_dir = models.FloatField(null=True,blank=True)
    pot_act_rev = models.FloatField(null=True,blank=True)
    pot_reac_cap_QI = models.FloatField(null=True, blank=True, max_length=5)
    pot_reac_cap_QII = models.FloatField(null=True, blank=True, max_length=5)
    pot_reac_cap_QIII = models.FloatField(null=True, blank=True, max_length=5)
    pot_reac_cap_QIV = models.FloatField(null=True, blank=True, max_length=5)
    pot_apar_dir = models.FloatField(null=True, blank=True, max_length=5)
    pot_apar_rev = models.FloatField(null=True, blank=True, max_length=5)
    vol_de_fase_1 = models.FloatField(null=True, blank=True, max_length=5)
    vol_de_fase_2 = models.FloatField(null=True, blank=True, max_length=5)
    vol_de_fase_3 = models.FloatField(null=True, blank=True, max_length=5)
    corriente_1 = models.FloatField(null=True, blank=True, max_length=5)
    corriente_2 = models.FloatField(null=True, blank=True, max_length=5)
    corriente_3 = models.FloatField(null=True, blank=True, max_length=5)
    fact_de_pot = models.FloatField(null=True, blank=True, max_length=5)
    fact_de_pot_1 = models.FloatField(null=True, blank=True, max_length=5)
    fact_de_pot_2 = models.FloatField(null=True, blank=True, max_length=5)
    fact_de_pot_3 = models.FloatField(null=True, blank=True, max_length=5)
    
    
    history = HistoricalRecords()
    
    def __str__(self):
        return self.name