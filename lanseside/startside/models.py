from django.db import models

class Lanse(models.Model):
    #lanse_nr = models.IntegerField()
    #ant_steg = models.IntegerField()
    #ant_akt = models.IntegerField()
    #auto_man = models.IntegerField()
    #man_steg = models.IntegerField()
    #trykk = models.IntegerField()

    lokal_maling = models.BooleanField(default=0)
    temperatur = models.IntegerField(default=0)
    vtrykk = models.IntegerField(default=0)
    ltrykk = models.IntegerField(default=0)
    flow = models.IntegerField(default=0)
    luftfukt = models.IntegerField(default=0)
    timestamp = models.IntegerField(default=0)

    plassering_bronn = models.IntegerField(default=0)
    lanse_kategori = models.IntegerField(default=0)
    auto_man = models.BooleanField(default=0)

    man_steg = models.IntegerField(default=0)


class Lansetyper(models.Model): 
    lanseid = models.IntegerField(default=0)
    lansetype = models.CharField(max_length=100,default='')
    ant_steg = models.IntegerField(default=0)


class LED(models.Model):
    stat = models.BooleanField()