# Generated by Django 2.0.2 on 2018-04-04 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startside', '0008_auto_20180404_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lanse',
            name='auto_man',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='lanse',
            name='flow',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='lanse',
            name='lanse_kategori',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='lanse',
            name='lokal_maling',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='lanse',
            name='luftfukt',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='lanse',
            name='man_steg',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='lanse',
            name='plassering_bronn',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='lanse',
            name='temperatur',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='lanse',
            name='timestamp',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='lanse',
            name='trykk',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='lansetyper',
            name='ant_steg',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='lansetyper',
            name='lanseid',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='lansetyper',
            name='lansetype',
            field=models.CharField(default='', max_length=100),
        ),
    ]
