# Generated by Django 2.0.1 on 2019-05-22 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_ncdbsampleyearly'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NcdbSampleYearly',
            new_name='NcdbSampleChanges',
        ),
    ]
