from django.db import models


class Lansetype(models.Model):
    class Meta:
        verbose_name_plural = "Lansetyper"

    lanseid = models.IntegerField(default=0)
    lansetype = models.CharField(max_length=32, null=True, default = "")
    ant_steg = models.IntegerField(default=0)

    def __str__(self):
        return str(self.lansetype)



class Lanse(models.Model):
    class Meta:
        verbose_name_plural = "Lanser"

    lokal_maling = models.BooleanField(default=0)
    temperatur_luft = models.FloatField(default=0)
    luftfukt = models.FloatField(default=0)

    temperatur_vann = models.FloatField(default=0)
    vanntrykk = models.FloatField(default=0)
    lufttrykk = models.FloatField(default=0)
    flow = models.FloatField(default=0)
    timestamp = models.FloatField(default=0)

    plassering_bronn = models.IntegerField(default=0)
    lanse_kategori = models.ForeignKey(Lansetype, null=True, on_delete=models.SET_NULL)
    auto_man = models.BooleanField(default=0)
    modus = models.IntegerField(default=0)

    def __str__(self):
        return str(self.plassering_bronn)



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



class langtidslagring(models.Model):
    class Meta:
        verbose_name_plural = "Logg"

    lanse = models.ForeignKey(Lanse, null=True, on_delete=models.SET_NULL)

    timestamp = models.FloatField(default=0)
    vanntrykk = models.FloatField(default=-1)
    steg = models.IntegerField(default=-1)
    #vanntrykk = models.FloatField(default=-1)

