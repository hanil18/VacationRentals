# Generated by Django 3.2.6 on 2021-10-07 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0009_auto_20191104_1554'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='country',
        ),
        migrations.RemoveField(
            model_name='room',
            name='room_type',
        ),
        migrations.DeleteModel(
            name='RoomType',
        ),
    ]
