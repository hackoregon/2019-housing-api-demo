# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class HmdaOrwa(models.Model):
    index = models.BigIntegerField(null=False, primary_key=True)
    year = models.TextField(blank=True, null=True)
    actiontakentype = models.TextField(db_column='ActionTakenType', blank=True, null=True)  # Field name made lowercase.
    agencyname = models.TextField(db_column='AgencyName', blank=True, null=True)  # Field name made lowercase.
    applicant1_sex_name = models.TextField(blank=True, null=True)
    applicant1race = models.TextField(db_column='Applicant1Race', blank=True, null=True)  # Field name made lowercase.
    applicant2_sex_name = models.TextField(blank=True, null=True)
    applicant2race = models.TextField(db_column='Applicant2Race', blank=True, null=True)  # Field name made lowercase.
    applicantincome = models.IntegerField(db_column='ApplicantIncome', blank=True, null=True)  # Field name made lowercase.
    censustract = models.TextField(db_column='CensusTract', blank=True, null=True)  # Field name made lowercase.
    countycode = models.TextField(db_column='CountyCode', blank=True, null=True)  # Field name made lowercase.
    denialreason1 = models.TextField(db_column='DenialReason1', blank=True, null=True)  # Field name made lowercase.
    denialreason2 = models.TextField(db_column='DenialReason2', blank=True, null=True)  # Field name made lowercase.
    denialreason3 = models.TextField(db_column='DenialReason3', blank=True, null=True)  # Field name made lowercase.
    editstatus = models.TextField(db_column='EditStatus', blank=True, null=True)  # Field name made lowercase.
    hoepa_loan = models.TextField(db_column='HOEPA_loan', blank=True, null=True)  # Field name made lowercase.
    hud_median_family_income = models.IntegerField(blank=True, null=True)
    lienstatus = models.TextField(db_column='LienStatus', blank=True, null=True)  # Field name made lowercase.
    loanamount = models.IntegerField(db_column='LoanAmount', blank=True, null=True)  # Field name made lowercase.
    loanpurpose = models.TextField(db_column='LoanPurpose', blank=True, null=True)  # Field name made lowercase.
    loantype = models.TextField(db_column='LoanType', blank=True, null=True)  # Field name made lowercase.
    minority_population = models.FloatField(blank=True, null=True)
    msaofproperty = models.TextField(db_column='MSAofProperty', blank=True, null=True)  # Field name made lowercase.
    number_of_1_to_4_family_units = models.IntegerField(blank=True, null=True)
    number_of_owner_occupied_units = models.IntegerField(blank=True, null=True)
    occupancy = models.TextField(db_column='Occupancy', blank=True, null=True)  # Field name made lowercase.
    population = models.IntegerField(blank=True, null=True)
    preapprovals = models.TextField(db_column='Preapprovals', blank=True, null=True)  # Field name made lowercase.
    propertytype = models.TextField(db_column='PropertyType', blank=True, null=True)  # Field name made lowercase.
    purchasertype = models.TextField(db_column='PurchaserType', blank=True, null=True)  # Field name made lowercase.
    ratespread = models.FloatField(db_column='RateSpread', blank=True, null=True)  # Field name made lowercase.
    respondent_id = models.TextField(db_column='Respondent_ID', blank=True, null=True)  # Field name made lowercase.
    sequencenumber = models.IntegerField(db_column='SequenceNumber', blank=True, null=True)  # Field name made lowercase.
    state = models.TextField(blank=True, null=True)
    tract_to_msamd_income = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hmda_orwa'
