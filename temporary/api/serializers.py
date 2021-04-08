from rest_framework import  serializers
from temporary.models import JobCategory, JobTitle, JobBrief, JobResponsibility, \
    JobRequirement, JobInterviewQuestion, City, Qualification, Skill, State, Country, Perks, Invoice, Payment, Plan, \
    SalesLead

""" Worked on 23.03.2021 """
class JobCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = JobCategory
        fields =('JobCategoryId', 'Name', 'Description', 'ApprovalFlag', 'ClientSpecificFlag', 'CreatedBy', 'CreatedDate', 'ModifiedBy', 'ModifiedDate', 'ActiveFlag')

class JobTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model=JobTitle
        fields=('JobTitleID', 'JobCategory', 'Name', 'Description', 'SuscriberId', 'ApprovalFlag', 'ClientSpecificFlag', 'CreatedBy', 'CreatedDate', 'ModifiedBy', 'ModifiedDate', 'ActiveFlag')

class JobBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model=JobBrief
        fields=('JobBriefID', 'JobTitleId', 'Name', 'Description', 'SuscriberId', 'ApprovalFlag', 'ClientSpecificFlag', 'CreatedBy', 'CreatedDate', 'ModifiedBy', 'ModifiedDate', 'ActiveFlag')

class JobResponsibilitySerializer(serializers.ModelSerializer):
    class Meta:
        model=JobResponsibility
        fields=('JobRolesResponsibilityID', 'JobTitleId', 'Name', 'Description', 'SuscriberId', 'ApprovalFlag', 'ClientSpecificFlag', 'CreatedBy', 'CreatedDate', 'ModifiedBy', 'ModifiedDate', 'ActiveFlag')

class JobRequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model=JobRequirement
        fields=('JobRequirementID', 'JobTitle', 'Name', 'Description', 'SuscriberId', 'ApprovalFlag', 'ClientSpecificFlag', 'CreatedBy', 'CreatedDate', 'ModifiedBy', 'ModifiedDate', 'ActiveFlag')


""" Worked on 24.03.2021 """


class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Qualification
        fields=('QualificationID', 'QualificationName', 'Description', 'SuscriberId', 'ApprovalFlag', 'ClientSpecificFlg', 'CreatedBy', 'CreatedDate', 'ModifiedBy', 'ModifiedDate', 'ActiveFlag')

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model=Skill
        fields=('SkillID','SkillName','Description','SuscriberId','ApprovalFlag',\
                'ClientSpecificFlg','CreatedBy','CreatedDate','ModifiedBy',\
                'ModifiedDate','ActiveFlag')

class PerksSerializer(serializers.ModelSerializer):
    class Meta:
        model=Perks
        fields=('PerksID','PerksName','Description','SuscriberId','ApprovalFlag',\
                'ClientSpecificFlg','CreatedBy','CreatedDate','ModifiedBy',\
                'ModifiedDate','ActiveFlag')


"""         25-03-2021        """
class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model=Plan
        fields=('PlanId','PlanType','PlanName','PlanEffectiveDate','NoOfDays',\
                'CreatedBy','CreatedDate','ModifiedBy','ModifiedDate',\
                'ActiveFlag')

class SalesLeadSerializer(serializers.ModelSerializer):
    class Meta:
        model=SalesLead
        fields=('SaledLeadId', 'CustomerName', 'CompanyIndividual', 'CompanyName', 'ContactNo', 'EmailId', 'Designation', 'LeadThru', 'CreatedBy', 'CreatedDate', 'ModifiedBy', 'ModifiedDate', 'ActiveFlag')

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Invoice
        fields=('InvoiceId','InvoiceDate','SubscriptionId','CustomerId','PlanId',\
                'InvoiceType','AdditionalUsers','UpgradePlanId','CreatedDate',\
                'ModifiedDate','CreatedBy','ModifiedBy')

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Payment
        fields=('PaymentId','PaymentDate','SubscriptionCode','InvoiceNo','InvoiceType',\
                'CustomerId','SalesOrderId','PaymentMode','PaymentDate',\
                'PayemntAmt','CreatedDate','ModifiedDate','CreatedBy','ModifiedBy')


"""
+++++++++++++++++++-+_+++
+++++++++++++++++++-+_+++
+++++++++++++++++++-+_+++
+++++++++++++++++++-+_+++
+++++++++++++++++++-+_+++
+++++++++++++++++++-+_+++
+++++++++++++++++++-+_+++
+++++++++++++++++++-+_+++
+++++++++++++++++++-+_+++
+++++++++++++++++++-+_+++
"""





class JobInterviewQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model=JobInterviewQuestion
        fields=('JobIntQuesCatCode','JobIntQuesTtlCode','JobIntQuesCode','JobIntQuesType','JobIntQuesDescription',\
                'JobIntQuesCreatedBy','JobIntQuesCreatedDate','JobIntQuesUpdatedBy','JobIntQuesUpdatedDate','JJobIntQuesDelFlag')


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model=City
        fields=('CityId','StateId','Name','Description','TimeZone',\
                'ActiveFlag')


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model=State
        fields=('StateId','CountryId','Name','Description','ActiveFlag')

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model=Country
        fields=('CountryId','CountryName','Description','ActiveFlag')

