from django.db import models

# Create your models here.

from django.db.models import CharField, DateField, BooleanField, IntegerField, FloatField, DecimalField, DurationField, \
    NullBooleanField,DateTimeField




class JobCategory(models.Model):
    JobCategoryId=CharField(max_length=15,primary_key=True)
    Name=CharField(max_length=200)
    Description=CharField(max_length=500)
    ApprovalFlag=BooleanField()
    ClientSpecificFlag=BooleanField()
    CreatedBy=CharField(max_length=50)
    CreatedDate=DateField(max_length=8,auto_now=True)
    ModifiedBy=CharField(max_length=50)
    ModifiedDate=DateField(max_length=8,auto_now=True)
    ActiveFlag=BooleanField(max_length=1)

    class Meta:
        db_table="JobCategory"

    def __str__(self):
        return str(self.JobCategoryCode)


class JobTitle(models.Model):
    JobTitleID=IntegerField(primary_key=True)
    JobCategory=CharField(max_length=10)
    Name=CharField(max_length=50)
    Description=CharField(max_length=500)
    SuscriberId=IntegerField()
    ApprovalFlag=BooleanField(max_length=1)
    ClientSpecificFlag=BooleanField(max_length=1,default=0)
    CreatedBy=CharField(max_length=50,null=True)
    CreatedDate=DateField(max_length=8)
    ModifiedBy=CharField(max_length=50,null=True)
    ModifiedDate=DateField(max_length=8)
    ActiveFlag=BooleanField(max_length=1)

    class Meta:
        db_table="JobTitle"

    def __str__(self):
        return str(self.JobTttleCode)


class JobResponsibility(models.Model):
    JobRolesResponsibilityID=IntegerField(primary_key=True)
    JobTitleId=IntegerField()
    Name=CharField(max_length=200)
    Description=CharField(max_length=500)
    SuscriberId=IntegerField()
    ApprovalFlag=BooleanField(default=0)
    ClientSpecificFlag=BooleanField(default=0)
    CreatedBy=CharField(max_length=200)
    CreatedDate=DateField(max_length=True,auto_now=True)
    ModifiedBy=CharField(max_length=200)
    ModifiedDate=DateField(max_length=True,auto_now=True)
    ActiveFlag=BooleanField(default=0)

    class Meta:
        db_table="JobResponsibility"

    def __str__(self):
        return str(self.JobResCatCode)


class JobRequirement(models.Model):
    JobRequirementID=IntegerField()
    JobTitle=CharField(max_length=500)
    Name=CharField(max_length=200)
    Description=CharField(max_length=500)
    SuscriberId=IntegerField()
    ApprovalFlag=BooleanField()
    ClientSpecificFlag=BooleanField()
    CreatedBy=CharField(max_length=200)
    CreatedDate=DateField(max_length=8,auto_now=True)
    ModifiedBy=CharField(max_length=200)
    ModifiedDate=DateField(max_length=8,auto_now=True)
    ActiveFlag=BooleanField(default=0)

    class Meta:
        db_table="JobRequirement"

    def __str__(self):
        return str(self.JobReqCode)

class JobBrief(models.Model):
    JobBriefID=IntegerField()
    JobTitleId=IntegerField()
    Name=CharField(max_length=200)
    Description=CharField(max_length=500)
    SuscriberId=IntegerField()
    ApprovalFlag=BooleanField(default=0)
    ClientSpecificFlag=BooleanField(default=0)
    CreatedBy=CharField(max_length=200)
    CreatedDate=DateField(max_length=8,auto_now=True)
    ModifiedBy=CharField(max_length=200)
    ModifiedDate=DateField(max_length=8,auto_now=True)
    ActiveFlag=BooleanField(default=0)

    class Meta:
        db_table="JobBrief"

    def __str__(self):
        return str(self.JobBrfCatCode)


class Qualification(models.Model):
    #primary_key=True QualificationID
    QualificationID=IntegerField()
    QualificationName=CharField(max_length=200)
    Description=CharField(max_length=500)
    SuscriberId=IntegerField()
    ApprovalFlag=BooleanField(default=0)
    ClientSpecificFlg=BooleanField(default=0)
    CreatedBy=CharField(max_length=200)
    CreatedDate=DateField(max_length=8,auto_now=True)
    ModifiedBy=CharField(max_length=200)
    ModifiedDate=DateField(max_length=8,auto_now=True)
    ActiveFlag=BooleanField(default=0)

    class Meta:
        db_table="Qualification"

    def __str__(self):
        return str(self.QualificationID)


class Skill(models.Model):
    SkillID=IntegerField()
    SkillName=CharField(max_length=200)
    Description=CharField(max_length=500)
    SuscriberId=IntegerField()
    ApprovalFlag=BooleanField(default=0)
    ClientSpecificFlg=BooleanField(default=0)
    CreatedBy=CharField(max_length=200)
    CreatedDate=DateField(max_length=8,auto_now=True)
    ModifiedBy=CharField(max_length=200)
    ModifiedDate=DateField(max_length=8,auto_now=True)
    ActiveFlag=BooleanField(default=0)

    class Meta:
        db_table="Skill"

    def __str__(self):
        return str(self.SkillID)


class Perks(models.Model):

    #primary_key=True Skill ID

    PerksID=IntegerField(primary_key=True)
    PerksName=CharField(max_length=200)
    Description=CharField(max_length=500)
    SuscriberId=IntegerField()
    ApprovalFlag=BooleanField(default=0)
    ClientSpecificFlg=BooleanField(default=0)
    CreatedBy=CharField(max_length=200)
    CreatedDate=DateField(max_length=8,auto_now=True)
    ModifiedBy=CharField(max_length=200)
    ModifiedDate=DateField(max_length=8,auto_now=True)
    ActiveFlag=BooleanField(default=0)

    class Meta:
        db_table="Perks"

    def __str__(self):
        return str(self.PerksID)

class Plan(models.Model):
    PlanId=IntegerField(primary_key=True)
    PlanType=CharField(max_length=150)
    PlanName=CharField(max_length=200)
    PlanEffectiveDate=DateField(max_length=8,auto_now=True)
    NoOfDays=IntegerField()
    CreatedBy=CharField(max_length=200)
    CreatedDate=DateField(max_length=8,auto_now=True)
    ModifiedBy=CharField(max_length=200)
    ModifiedDate=DateField(max_length=8,auto_now=True)
    ActiveFlag=BooleanField(default=0)

    class Meta:
        db_table="Plan"

    def __str__(self):
        return str(self.PlanId)

#SalesLead,
class SalesLead(models.Model):
    SaledLeadId=IntegerField()
    CustomerName=CharField(max_length=200)
    CompanyIndividual=CharField(max_length=200)
    CompanyName=CharField(max_length=500)
    ContactNo=CharField(max_length=10)
    EmailId=CharField(max_length=150)
    Designation=CharField(max_length=200)
    LeadThru=CharField(max_length=200)
    CreatedBy=CharField(max_length=200)
    CreatedDate=DateField(max_length=8,auto_now=True)
    ModifiedBy=CharField(max_length=200)
    ModifiedDate=DateField(max_length=8,auto_now=True)
    ActiveFlag=BooleanField(default=0)

    class Meta:
        db_table="SalesLead"

    def __str__(self):
        return str(self.SalesLeadId)


class Invoice(models.Model):
    InvoiceId=IntegerField(primary_key=True)
    InvoiceDate=DateField(max_length=8,auto_now=True)
    SubscriptionId=IntegerField()
    CustomerId=IntegerField()
    PlanId=IntegerField()
    InvoiceType=CharField(max_length=150)
    AdditionalUsers=CharField(max_length=200)
    UpgradePlanId=IntegerField()
    CreatedDate=DateField(max_length=8,auto_now=True)
    ModifiedDate=DateField(max_length=8,auto_now=True)
    CreatedBy=CharField(max_length=200)
    ModifiedBy=CharField(max_length=200)

    class Meta:
        db_table="Invoice"

    def __str__(self):
        return self.InvoiceId

class Payment(models.Model):

    PaymentId=IntegerField(primary_key=True)
    PaymentDate=DateField(max_length=8,auto_now=True)
    SubscriptionCode=IntegerField()
    InvoiceNo=IntegerField()
    InvoiceType=CharField(max_length=150)
    CustomerId=IntegerField()
    SalesOrderId=IntegerField()
    PaymentMode=CharField(max_length=200)
    PaymentDate=DateField(max_length=8,auto_now=True)
    PayemntAmt=DecimalField(decimal_places=2,max_digits=10)
    CreatedDate=DateField(max_length=8,auto_now=True)
    ModifiedDate=DateField(max_length=8,auto_now=True)
    CreatedBy=CharField(max_length=200)
    ModifiedBy=CharField(max_length=200)


    class Meta:
        db_table="Payment"

    def __str__(self):
        return self.PaymentId


#_________________________________________________________________________________________________________




class JobInterviewQuestion(models.Model):
    JobIntQuesCatCode=CharField(max_length=10)
    JobIntQuesTtlCode=CharField(max_length=10)#models.ForeignKey(to=JobTitle,on_delete=models.CASCADE)
    JobIntQuesCode=CharField(max_length=10,primary_key=True)
    JobIntQuesType=CharField(max_length=100)
    JobIntQuesDescription=CharField(max_length=250)
    JobIntQuesCreatedBy=CharField(max_length=50)
    JobIntQuesCreatedDate=DateField(max_length=8)
    JobIntQuesUpdatedBy=CharField(max_length=50)
    JobIntQuesUpdatedDate=DateField(max_length=8)
    JJobIntQuesDelFlag=BooleanField(max_length=10)

    class Meta:
        db_table="JobInterviewQuestion"

    def __str__(self):
        return self.JobIntQuesCatCode


class TranJobBrief(models.Model):
    TransJobBriefId=IntegerField(primary_key=True)
    TransJDId=IntegerField()
    SubscriptionId=IntegerField()
    TransJobBriefDescription=CharField(max_length=200)

    class Meta:
        db_table="TranJobBrief"

    def __str__(self):
        return self.TranJobBriefId

class TranJobRoles(models.Model):
    TransJobRolesID=IntegerField()
    TransJDId=IntegerField()
    SubscriptionId=IntegerField()
    TransJobRolesDescription=CharField(max_length=200)

    class Meta:
        db_table="TransJobRoles"

    def __str__(self):
        return self.TransJobRolesID

class TranJobPerks(models.Model):
    TransJobPerksId=IntegerField()
    TransJDId=IntegerField()
    SubscriptionId=IntegerField()
    TransJobPerksDescription=CharField(max_length=200)

    class Meta:
        db_table="TranJobPerks"

    def __str__(self):
        return self.TransJobPerksId

class TranJobJD(models.Model):
    TransJDId=CharField(max_length=100)#models.ForeignKey()#to_fields="TransJobBriefId",)#IntegerField(primary_key=True)
    TransJDDate=DateField()
    SubscriptionId=IntegerField()
    ClientId=IntegerField()
    JdCategoryId=IntegerField()
    JdJobBriefId=IntegerField()
    JdJobTitleId=IntegerField()
    JdJobRequirementId=IntegerField()
    JdJobRolesId=IntegerField()
    JdJobPerks=CharField(max_length=200)
    Education=CharField(max_length=200)
    JDJobSkillId=IntegerField()
    JDSkillImportance=CharField(max_length=200)
    MinExperience=FloatField()
    Compensation=FloatField()
    Salary=FloatField()
    WorkLocation=CharField(max_length=200)
    TimeZone=DateTimeField()
    JDTemplateId=IntegerField()
    JDContent=CharField(max_length=300)
    JDCreatedBy=CharField(max_length=200)
    JDCreatedDate=DateField()
    JDModifiedBy=CharField(max_length=200)
    JDModifiedDate=DateField()

    class Meta:
        db_table = "TranJobJD"

    def __str__(self):
        return self.TransJDId


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#24-03-2021 api's



class City(models.Model):

    #CityId is primary_key

    CityId=IntegerField(primary_key=True)#IntegerField(primary_key=True)
    StateId=IntegerField()
    Name=CharField(max_length=200)
    Description=CharField(max_length=500)
    TimeZone=DateTimeField()
    ActiveFlag=BooleanField(default=0)

    class Meta:
        db_table="City"

    def __str__(self):
        return self.CityId


class State(models.Model):

    StateId=IntegerField(primary_key=True)#models.ForeignKey(to=City)
    CountryId=IntegerField()
    Name=CharField(max_length=200)
    Description=CharField(max_length=500)
    ActiveFlag=BooleanField(default=0)

    class Meta:
        db_table="State"

    def __str__(self):
        return self.StateId


class Country(models.Model):

    #primary_key=True CountryId

    CountryId=IntegerField(primary_key=True)#models.ForeignKey(to=State)#
    CountryName=CharField(max_length=200)
    Description=CharField(max_length=500)
    ActiveFlag=BooleanField(default=0)

    class Meta:
        db_table="Country"

    def __str__(self):
        return self.CountryId
