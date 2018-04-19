from django.db import models

class Lanse(models.Model):
    #lanse_nr = models.IntegerField()
    #ant_steg = models.IntegerField()
    #ant_akt = models.IntegerField()
    #auto_man = models.IntegerField()
    #man_steg = models.IntegerField()
    #trykk = models.IntegerField()

    lokal_maling = models.BooleanField(default=0)
    temperatur = models.FloatField(default=0)
    vtrykk = models.FloatField(default=0)
    ltrykk = models.FloatField(default=0)
    flow = models.FloatField(default=0)
    luftfukt = models.FloatField(default=0)
    timestamp = models.FloatField(default=0)

    plassering_bronn = models.IntegerField(default=0)
    lanse_kategori = models.IntegerField(default=0)
    auto_man = models.BooleanField(default=0)

    man_steg = models.IntegerField(default=0)


class Lansetyper(models.Model): 
    lanseid = models.IntegerField(default=0)
    lansetype = models.CharField(max_length=100,default='')
    ant_steg = models.IntegerField(default=0)


class Verdata(models.Model):
    dew_2 = models.IntegerField(default=0)
    dew_1 = models.IntegerField(default=0)
    dew = models.IntegerField(default=0)
    temp = models.IntegerField(default=0)
    hum = models.IntegerField(default=0)
    press = models.IntegerField(default=0)
    wind = models.IntegerField(default=0)
    gust = models.IntegerField(default=0)
    windDir = models.IntegerField(default=0)
    windChill = models.IntegerField(default=0)
    rain = models.IntegerField(default=0)
    rainRate = models.IntegerField(default=0)
    temp_1 = models.IntegerField(default=0)
    temp2_1 = models.IntegerField(default=0)
    hum_1 = models.IntegerField(default=0)
    temp_2 = models.IntegerField(default=0)
    temp2_2 = models.IntegerField(default=0)
    hum_2 = models.IntegerField(default=0)
    timestamp = models.IntegerField(default=0)