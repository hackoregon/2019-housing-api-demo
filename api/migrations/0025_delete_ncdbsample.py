# Generated by Django 2.0.1 on 2019-05-28 03:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_auto_20190528_0330'),
    ]

    operations = [
        migrations.DeleteModel(
            name='NcdbSample',
        ),
    ]