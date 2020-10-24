# Generated by Django 3.0 on 2020-09-04 13:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Schedule', '0003_auto_20200904_2056'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='날짜'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='time',
            field=models.TimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='시간'),
        ),
    ]
