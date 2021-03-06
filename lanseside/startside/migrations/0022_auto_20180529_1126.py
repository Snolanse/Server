# Generated by Django 2.0.2 on 2018-05-29 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startside', '0021_auto_20180424_1545'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='categori',
        ),
        migrations.AlterModelOptions(
            name='langtidslagring',
            options={'verbose_name_plural': 'Logg'},
        ),
        migrations.AlterField(
            model_name='verdata',
            name='dew',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='verdata',
            name='dew_1',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='verdata',
            name='dew_2',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='verdata',
            name='gust',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='verdata',
            name='hum_1',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='verdata',
            name='hum_2',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='verdata',
            name='press',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='verdata',
            name='rain',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='verdata',
            name='rainRate',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='verdata',
            name='temp',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='verdata',
            name='temp2_1',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='verdata',
            name='temp2_2',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='verdata',
            name='temp_1',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='verdata',
            name='temp_2',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='verdata',
            name='timestamp',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='verdata',
            name='wind',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='verdata',
            name='windChill',
            field=models.FloatField(default=0),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='test',
        ),
    ]
