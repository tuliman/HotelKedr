# Generated by Django 3.0.2 on 2020-01-30 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kedr', '0003_auto_20200130_2258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apartment',
            name='photo_obj',
        ),
        migrations.AddField(
            model_name='photo',
            name='apartment_obj',
            field=models.ManyToManyField(to='kedr.Apartment'),
        ),
    ]
