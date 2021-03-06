# Generated by Django 2.0.1 on 2019-07-17 04:03

from django.db import migrations

def add_population_addendum(apps, schema_editor):
    addendum = apps.get_model("api", "NcdbPopulationAddendum")
    yearly = apps.get_model("api", "NcdbSampleYearly")
    count = addendum.objects.all().count()
    for addendum_instance in addendum.objects.all():
        for yearly_instance in yearly.objects.filter(fips_code=addendum_instance.geo_fips):
            print(".")
            if yearly_instance.year == 1990:
                yearly_instance.population = addendum_instance.totalpopulation_90
            elif yearly_instance.year == 2000:
                yearly_instance.population = addendum_instance.totalpopulation_00
            elif yearly_instance.year == 2010:
                yearly_instance.population = addendum_instance.totalpopulation_10
            elif yearly_instance.year == 2017:
                yearly_instance.population = addendum_instance.totalpopulation_17
            yearly_instance.save()
        print(str(round(addendum_instance.index / count * 10000) / 100) + "%")

class Migration(migrations.Migration):

    dependencies = [
        ('api', '0029_auto_20190717_0401'),
    ]

    operations = [
        migrations.RunPython(add_population_addendum)
    ]
