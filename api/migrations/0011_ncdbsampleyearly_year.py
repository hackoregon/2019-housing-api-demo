# Generated by Django 2.0.1 on 2019-05-23 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20190523_0204'),
    ]

    operations = [
        migrations.AddField(
            model_name='ncdbsampleyearly',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
