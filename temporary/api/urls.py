from django.conf.urls import url
from . import views
from .views import JobCategoryListView, JobCategoryCreateApi, JobCategoryDetailView, \
    JobTitleListView, JobTitleDetailView, JobTitleCreateApi, JobTitleUpdateApi, JobTitleDeleteApi, JobBriefListView, \
    JobBriefDetailView, JobBriefCreateApi, JobBriefUpdateApi, JobBriefDeleteApi, JobResponsibilityListView, \
    JobResponsibilityDetailView, JobResponsibilityCreateApi, JobResponsibilityUpdateApi, JobResponsibilityDeleteApi, \
    JobRequirementListView, JobRequirementDetailView, JobRequirementCreateApi, JobRequirementUpdateApi, \
    JobRequirementDeleteApi, JobInterviewQuestionListView, JobInterviewQuestionDetailView, \
    JobInterviewQuestionCreateApi, JobInterviewQuestionUpdateApi, JobInterviewQuestionDeleteApi, \
    CityListView, CityDetailView, \
    CityCreateApi, CityUpdateApi, CityDeleteApi, StateListView, StateDetailView, StateCreateApi, StateUpdateApi, \
    StateDeleteApi, CountryListView, CountryDetailView, CountryCreateApi, CountryUpdateApi, CountryDeleteApi, \
    QualificationListView, QualificationDetailView, QualificationCreateApi, QualificationUpdateApi, \
    QualificationDeleteApi, SkillListView, SkillDetailView, SkillCreateApi, SkillUpdateApi, SkillDeleteApi, \
    PerksListView, PerksDetailView, PerksCreateApi, PerksUpdateApi, PerksDeleteApi, InvoiceDeleteApi, InvoiceUpdateApi, \
    InvoiceCreateApi, InvoiceDetailView, InvoiceListView, PaymentListView, PaymentDetailView, PaymentCreateApi, \
    PaymentUpdateApi, PaymentDeleteApi, PlanListView, PlanDetailView, PlanCreateApi, PlanUpdateApi, PlanDeleteApi, \
    SalesLeadListView, SalesLeadDetailView, SalesLeadCreateApi, SalesLeadUpdateApi, SalesLeadDeleteApi

urlpatterns = [

    #Job Category
    url(r'^jobcategory/$',JobCategoryListView.as_view()),
    url(r'^detailed/jobcategory/(?P<pk>[-\w]+)', JobCategoryDetailView.as_view()),
    url(r'^create/jobcategory/$',JobCategoryCreateApi.as_view()),
    url(r'^update/jobcategory/(?P<pk>[-\w]+)',views.JobCategoryUpdateApi.as_view()),
    url(r'^delete/jobcategory/(?P<pk>[-\w]+)',views.JobCategoryDeleteApi.as_view()),


    # Job Title
    url(r'^jobtitle/$',JobTitleListView.as_view()),
    url(r'^detailed/jobtitle/(?P<pk>[-\w]+)', JobTitleDetailView.as_view()),
    url(r'^create/jobtitle/$',JobTitleCreateApi.as_view()),
    url(r'^update/jobtitle/(?P<pk>[-\w]+)',JobTitleUpdateApi.as_view()),
    url(r'^delete/jobtitle/(?P<pk>[-\w]+)',JobTitleDeleteApi.as_view()),

    # Job Brief
    url(r'^jobbrief/$', JobBriefListView.as_view()),
    url(r'^detailed/jobbrief/(?P<pk>[-\w]+)', JobBriefDetailView.as_view()),
    url(r'^create/jobbrief/$', JobBriefCreateApi.as_view()),
    url(r'^update/jobbrief/(?P<pk>[-\w]+)', JobBriefUpdateApi.as_view()),
    url(r'^delete/jobbrief/(?P<pk>[-\w]+)', JobBriefDeleteApi.as_view()),

    # Job Responsiblity
    url(r'^jobresponsibility/$', JobResponsibilityListView.as_view()),
    url(r'^detailed/jobresponsibility/(?P<pk>[-\w]+)', JobResponsibilityDetailView.as_view()),
    url(r'^create/jobresponsibility/$', JobResponsibilityCreateApi.as_view()),
    url(r'^update/jobresponsibility/(?P<pk>[-\w]+)', JobResponsibilityUpdateApi.as_view()),
    url(r'^delete/jobresponsibility/(?P<pk>[-\w]+)', JobResponsibilityDeleteApi.as_view()),

    # Job Requirement
    url(r'^jobrequirement/$', JobRequirementListView.as_view()),
    url(r'^detailed/jobrequirement/(?P<pk>[-\w]+)', JobRequirementDetailView.as_view()),
    url(r'^create/jobrequirement/$', JobRequirementCreateApi.as_view()),
    url(r'^update/jobrequirement/(?P<pk>[-\w]+)', JobRequirementUpdateApi.as_view()),
    url(r'^delete/jobrequirement/(?P<pk>[-\w]+)', JobRequirementDeleteApi.as_view()),

    # Job InterviewQuestion
    url(r'^jobinterviewquestion/$', JobInterviewQuestionListView.as_view()),
    url(r'^detailed/jobinterviewquestion/(?P<pk>[-\w]+)', JobInterviewQuestionDetailView.as_view()),
    url(r'^create/jobinterviewquestion/$', JobInterviewQuestionCreateApi.as_view()),
    url(r'^update/jobinterviewquestion/(?P<pk>[-\w]+)', JobInterviewQuestionUpdateApi.as_view()),
    url(r'^delete/jobinterviewquestion/(?P<pk>[-\w]+)', JobInterviewQuestionDeleteApi.as_view()),


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 24-03-2021

    # City
    url(r'^city/$', CityListView.as_view()),
    url(r'^detailed/city/(?P<pk>[-\w]+)', CityDetailView.as_view()),
    url(r'^create/city/$', CityCreateApi.as_view()),
    url(r'^update/city/(?P<pk>[-\w]+)', CityUpdateApi.as_view()),
    url(r'^delete/city/(?P<pk>[-\w]+)', CityDeleteApi.as_view()),

    # State
    url(r'^state/$', StateListView.as_view()),
    url(r'^detailed/state/(?P<pk>[-\w]+)', StateDetailView.as_view()),
    url(r'^create/state/$', StateCreateApi.as_view()),
    url(r'^update/state/(?P<pk>[-\w]+)', StateUpdateApi.as_view()),
    url(r'^delete/state/(?P<pk>[-\w]+)', StateDeleteApi.as_view()),

    # country
    url(r'^country/$', CountryListView.as_view()),
    url(r'^detailed/country/(?P<pk>[-\w]+)', CountryDetailView.as_view()),
    url(r'^create/country/$', CountryCreateApi.as_view()),
    url(r'^update/country/(?P<pk>[-\w]+)', CountryUpdateApi.as_view()),
    url(r'^delete/country/(?P<pk>[-\w]+)', CountryDeleteApi.as_view()),

    # qualification
    url(r'^qualification/$', QualificationListView.as_view()),
    url(r'^detailed/qualification/(?P<pk>[-\w]+)', QualificationDetailView.as_view()),
    url(r'^create/qualification/$', QualificationCreateApi.as_view()),
    url(r'^update/qualification/(?P<pk>[-\w]+)', QualificationUpdateApi.as_view()),
    url(r'^delete/qualification/(?P<pk>[-\w]+)', QualificationDeleteApi.as_view()),

    # skill
    url(r'^skill/$', SkillListView.as_view()),
    url(r'^detailed/skill/(?P<pk>[-\w]+)', SkillDetailView.as_view()),
    url(r'^create/skill/$', SkillCreateApi.as_view()),
    url(r'^update/skill/(?P<pk>[-\w]+)', SkillUpdateApi.as_view()),
    url(r'^delete/skill/(?P<pk>[-\w]+)', SkillDeleteApi.as_view()),

    # perks
    url(r'^perks/$', PerksListView.as_view()),
    url(r'^detailed/perks/(?P<pk>[-\w]+)', PerksDetailView.as_view()),
    url(r'^create/perks/$', PerksCreateApi.as_view()),
    url(r'^update/perks/(?P<pk>[-\w]+)', PerksUpdateApi.as_view()),
    url(r'^delete/perks/(?P<pk>[-\w]+)', PerksDeleteApi.as_view()),

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 25-03-2021


    url(r'^invoice/$', InvoiceListView.as_view()),
    url(r'^detailed/invoice/(?P<pk>[-\w]+)', InvoiceDetailView.as_view()),
    url(r'^create/invoice/$', InvoiceCreateApi.as_view()),
    url(r'^update/invoice/(?P<pk>[-\w]+)', InvoiceUpdateApi.as_view()),
    url(r'^delete/invoice/(?P<pk>[-\w]+)', InvoiceDeleteApi.as_view()),


    url(r'^payment/$', PaymentListView.as_view()),
    url(r'^detailed/payment/(?P<pk>[-\w]+)', PaymentDetailView.as_view()),
    url(r'^create/payment/$', PaymentCreateApi.as_view()),
    url(r'^update/payment/(?P<pk>[-\w]+)', PaymentUpdateApi.as_view()),
    url(r'^delete/payment/(?P<pk>[-\w]+)', PaymentDeleteApi.as_view()),

    url(r'^plan/$', PlanListView.as_view()),
    url(r'^detailed/plan/(?P<pk>[-\w]+)', PlanDetailView.as_view()),
    url(r'^create/plan/$', PlanCreateApi.as_view()),
    url(r'^update/plan/(?P<pk>[-\w]+)', PlanUpdateApi.as_view()),
    url(r'^delete/plan/(?P<pk>[-\w]+)', PlanDeleteApi.as_view()),

    url(r'^saleslead/$', SalesLeadListView.as_view()),
    url(r'^detailed/saleslead/(?P<pk>[-\w]+)', SalesLeadDetailView.as_view()),
    url(r'^create/saleslead/$', SalesLeadCreateApi.as_view()),
    url(r'^update/saleslead/(?P<pk>[-\w]+)', SalesLeadUpdateApi.as_view()),
    url(r'^delete/saleslead/(?P<pk>[-\w]+)', SalesLeadDeleteApi.as_view())

]
