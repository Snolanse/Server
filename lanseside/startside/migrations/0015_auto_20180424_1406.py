# Generated by Django 2.0.2 on 2018-04-24 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startside', '0014_auto_20180420_1524'),
    ]

    operations = [
        migrations.CreateModel(
            name='langtidslagring',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.FloatField(default=0)),
                ('steg', models.IntegerField(default=-1)),
                ('vanntrykk', models.FloatField(default=-1)),
            ],
        ),
        migrations.AlterModelOptions(
            name='lanse',
            options={'verbose_name_plural': 'Lanser'},
        ),
        migrations.AlterModelOptions(
            name='lansetyper',
            options={'verbose_name_plural': 'Lansetyper'},
        ),
    ]
