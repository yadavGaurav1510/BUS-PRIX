# Generated by Django 3.2.7 on 2021-09-27 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='seatsEmpty',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]