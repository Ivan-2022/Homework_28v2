# Generated by Django 4.1.1 on 2022-10-05 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_location_lat_alter_location_lng'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='locations',
            new_name='location',
        ),
    ]