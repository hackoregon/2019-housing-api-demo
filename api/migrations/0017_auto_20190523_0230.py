# Generated by Django 2.0.1 on 2019-05-23 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_auto_20190523_0229'),
    ]

    operations = [
        migrations.AddField(
            model_name='ncdbsamplechanges',
            name='end_year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ncdbsamplechanges',
            name='start_year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
