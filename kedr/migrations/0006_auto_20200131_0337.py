# Generated by Django 3.0.2 on 2020-01-31 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kedr', '0005_auto_20200131_0314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='apartment_obj',
        ),
        migrations.AddField(
            model_name='apartment',
            name='apartment_obj',
            field=models.ManyToManyField(related_name='images', to='kedr.Photo'),
        ),
    ]
