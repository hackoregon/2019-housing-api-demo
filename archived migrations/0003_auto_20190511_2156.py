# Generated by Django 2.0.1 on 2019-05-11 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190511_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='ncdbsampleyearly',
            name='asothshare',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ncdbsampleyearly',
            name='bachshare',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ncdbsampleyearly',
            name='blackshare',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ncdbsampleyearly',
            name='hispshare',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ncdbsampleyearly',
            name='medhomeval',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ncdbsampleyearly',
            name='medinc',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ncdbsampleyearly',
            name='medrentval',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ncdbsampleyearly',
            name='metasothshare',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ncdbsampleyearly',
            name='metbachshare',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ncdbsampleyearly',
            name='metblackshare',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ncdbsampleyearly',
            name='methispshare',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ncdbsampleyearly',
            name='metmedhomeval',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ncdbsampleyearly',
            name='metmedinc',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ncdbsampleyearly',
            name='metmedrentval',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ncdbsampleyearly',
            name='metownshare',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ncdbsampleyearly',
            name='metpovrate',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ncdbsampleyearly',
            name='metrentcbshare',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ncdbsampleyearly',
            name='metwhiteshare',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ncdbsampleyearly',
            name='ownshare',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ncdbsampleyearly',
            name='povrate',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ncdbsampleyearly',
            name='rentcbshare',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ncdbsampleyearly',
            name='whiteshare',
            field=models.FloatField(blank=True, null=True),
        ),
    ]