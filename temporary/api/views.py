from rest_framework import generics, permissions
from ..models import JobCategory, JobTitle, JobBrief, JobResponsibility, JobRequirement, JobInterviewQuestion, \
    City, Qualification, Skill, Perks, State, Country, Invoice, Payment, Plan, SalesLead
from .serializers import JobCategorySerializer, JobTitleSerializer, JobBriefSerializer, \
    JobResponsibilitySerializer, JobRequirementSerializer, JobInterviewQuestionSerializer, \
    CitySerializer, QualificationSerializer, SkillSerializer, PerksSerializer, StateSerializer, CountrySerializer, \
    InvoiceSerializer, PaymentSerializer, PlanSerializer, SalesLeadSerializer
from rest_framework import generics


class JobCategoryListView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'head', 'post']

    queryset = JobCategory.objects.all()
    serializer_class = JobCategorySerializer


class JobCategoryDetailView(generics.RetrieveAPIView):
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'head', 'post']

    queryset = JobCategory.objects.all()
    serializer_class = JobCategorySerializer


class JobCategoryCreateApi(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'head', 'post']

    queryset = JobCategory.objects.all()
    serializer_class = JobCategorySerializer


class JobCategoryUpdateApi(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.AllowAny,)

    queryset = JobCategory.objects.all()
    serializer_class = JobCategorySerializer


class JobCategoryDeleteApi(generics.DestroyAPIView):
    permission_classes = (permissions.AllowAny,)

    queryset = JobCategory.objects.all()
    serializer_class = JobCategorySerializer


##########################################################################################


class JobTitleListView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'head', 'post']

    queryset = JobTitle.objects.all()
    serializer_class = JobTitleSerializer


class JobTitleDetailView(generics.RetrieveAPIView):
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'head', 'post']

    queryset = JobTitle.objects.all()
    serializer_class = JobTitleSerializer


class JobTitleCreateApi(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'head', 'post']

    queryset = JobTitle.objects.all()
    serializer_class = JobTitleSerializer


class JobTitleUpdateApi(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.AllowAny,)

    queryset = JobTitle.objects.all()
    serializer_class = JobTitleSerializer


class JobTitleDeleteApi(generics.DestroyAPIView):
    permission_classes = (permissions.AllowAny,)

    queryset = JobTitle.objects.all()
    serializer_class = JobTitleSerializer


"""  Job Brief goes here >>>>>>>>>>>>>>>>>>>>>>>>>>"""

class JobBriefListView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'head', 'post']

    queryset =JobBrief.objects.all()
    serializer_class = JobBriefSerializer

class JobBriefDetailView(generics.RetrieveAPIView):
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'head', 'post']

    queryset = JobBrief.objects.all()
    serializer_class = JobBriefSerializer

class JobBriefCreateApi(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'head', 'post']

    queryset = JobBrief.objects.all()
    serializer_class = JobBriefSerializer

class JobBriefUpdateApi(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.AllowAny,)

    queryset = JobBrief.objects.all()
    serializer_class = JobBriefSerializer

class JobBriefDeleteApi(generics.DestroyAPIView):
    permission_classes = (permissions.AllowAny,)

    queryset = JobBrief.objects.all()
    serializer_class = JobBriefSerializer

"""  Job Responsiblity goes here!.................."""


class JobResponsibilityListView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'head', 'post']

    queryset =JobResponsibility.objects.all()
    serializer_class = JobResponsibilitySerializer



class JobResponsibilityDetailView(generics.RetrieveAPIView):
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'head', 'post']

    queryset = JobResponsibility.objects.all()
    serializer_class = JobResponsibilitySerializer

class JobResponsibilityCreateApi(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'head', 'post']

    queryset = JobResponsibility.objects.all()
    serializer_class = JobResponsibilitySerializer

class JobResponsibilityUpdateApi(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.AllowAny,)

    queryset = JobResponsibility.objects.all()
    serializer_class = JobResponsibilitySerializer

class JobResponsibilityDeleteApi(generics.DestroyAPIView):
    permission_classes = (permissions.AllowAny,)

    queryset = JobResponsibility.objects.all()
    serializer_class = JobResponsibilitySerializer


"""  Job Requirement goes here >>>>>>>>>>>>>>>>>>>>>> """

class JobRequirementListView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'head', 'post']

    queryset =JobRequirement.objects.all()
    serializer_class = JobRequirementSerializer



class JobRequirementDetailView(generics.RetrieveAPIView):
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'head', 'post']

    queryset = JobRequirement.objects.all()
    serializer_class = JobRequirementSerializer

class JobRequirementCreateApi(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'head', 'post']

    queryset = JobRequirement.objects.all()
    serializer_class = JobRequirementSerializer

class JobRequirementUpdateApi(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.AllowAny,)

    queryset = JobRequirement.objects.all()
    serializer_class = JobRequirementSerializer

class JobRequirementDeleteApi(generics.DestroyAPIView):
    permission_classes = (permissions.AllowAny,)

    queryset = JobRequirement.objects.all()
    serializer_class = JobRequirementSerializer


""" Job Interview Question goes here >>>>>>>>>>>>>>>>.  """
class JobInterviewQuestionListView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'head', 'post']

    queryset =JobInterviewQuestion.objects.all()
    serializer_class = JobInterviewQuestionSerializer

class JobInterviewQuestionDetailView(generics.RetrieveAPIView):
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'head', 'post']

    queryset = JobInterviewQuestion.objects.all()
    serializer_class = JobInterviewQuestionSerializer

class JobInterviewQuestionCreateApi(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'head', 'post']

    queryset = JobInterviewQuestion.objects.all()
    serializer_class = JobInterviewQuestionSerializer

class JobInterviewQuestionUpdateApi(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.AllowAny,)

    queryset = JobInterviewQuestion.objects.all()
    serializer_class = JobInterviewQuestionSerializer

class JobInterviewQuestionDeleteApi(generics.DestroyAPIView):
    permission_classes = (permissions.AllowAny,)

    queryset = JobInterviewQuestion.objects.all()
    serializer_class = JobInterviewQuestionSerializer



"""  City goes here >>>>>>>>>>>>>>>>>>>> """

class CityListView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'head', 'post']

    queryset =City.objects.all()
    serializer_class = CitySerializer


class CityDetailView(generics.RetrieveAPIView):
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'head', 'post']

    queryset = City.objects.all()
    serializer_class = CitySerializer

class CityCreateApi(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'head', 'post']

    queryset = City.objects.all()
    serializer_class = CitySerializer

class CityUpdateApi(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.AllowAny,)

    queryset = City.objects.all()
    serializer_class = CitySerializer

class CityDeleteApi(generics.DestroyAPIView):
    permission_classes = (permissions.AllowAny,)

    queryset = City.objects.all()
    serializer_class = CitySerializer


"""  State goes here >>>>>>>>>>>>>>>>>>>> """

class StateListView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'head', 'post']

    queryset =State.objects.all()
    serializer_class = StateSerializer


class StateDetailView(generics.RetrieveAPIView):
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'head', 'post']

    queryset = State.objects.all()
    serializer_class = StateSerializer

class StateCreateApi(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'head', 'post']

    queryset = State.objects.all()
    serializer_class = StateSerializer

class StateUpdateApi(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.AllowAny,)

    queryset = State.objects.all()
    serializer_class = StateSerializer

class StateDeleteApi(generics.DestroyAPIView):
    permission_classes = (permissions.AllowAny,)

    queryset = State.objects.all()
    serializer_class = StateSerializer


"""  Country goes here >>>>>>>>>>>>>>>>>>>> """

class CountryListView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'head', 'post']

    queryset =Country.objects.all()
    serializer_class = CountrySerializer


class CountryDetailView(generics.RetrieveAPIView):
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'head', 'post']

    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class CountryCreateApi(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'head', 'post']

    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class CountryUpdateApi(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.AllowAny,)

    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class CountryDeleteApi(generics.DestroyAPIView):
    permission_classes = (permissions.AllowAny,)

    queryset = Country.objects.all()
    serializer_class = CountrySerializer


""" Qualification goes here >>>>>>>>>>>>>>>>>>>>>> """

class QualificationListView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'head', 'post']

    queryset =Qualification.objects.all()
    serializer_class = QualificationSerializer


class QualificationDetailView(generics.RetrieveAPIView):
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'head', 'post']

    queryset = Qualification.objects.all()
    serializer_class = QualificationSerializer

class QualificationCreateApi(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'head', 'post']

    queryset = Qualification.objects.all()
    serializer_class = QualificationSerializer

class QualificationUpdateApi(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.AllowAny,)

    queryset = Qualification.objects.all()
    serializer_class = QualificationSerializer

class QualificationDeleteApi(generics.DestroyAPIView):
    permission_classes = (permissions.AllowAny,)

    queryset = Qualification.objects.all()
    serializer_class = QualificationSerializer

""" Skill goes here >>>>>>>>>>>>>>>>>>>>.. """

class SkillListView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'head', 'post']

    queryset =Skill.objects.all()
    serializer_class = SkillSerializer


class SkillDetailView(generics.RetrieveAPIView):
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'head', 'post']

    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class SkillCreateApi(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'head', 'post']

    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class SkillUpdateApi(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.AllowAny,)

    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class SkillDeleteApi(generics.DestroyAPIView):
    permission_classes = (permissions.AllowAny,)

    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

""" Perks goes here >>>>>>>>>>>>>>>>>>>> """

class PerksListView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'head', 'post']

    queryset =Perks.objects.all()
    serializer_class = PerksSerializer


class PerksDetailView(generics.RetrieveAPIView):
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'head', 'post']

    queryset = Perks.objects.all()
    serializer_class = PerksSerializer

class PerksCreateApi(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'head', 'post']

    queryset = Perks.objects.all()
    serializer_class = PerksSerializer

class PerksUpdateApi(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.AllowAny,)

    queryset = Perks.objects.all()
    serializer_class = PerksSerializer

class PerksDeleteApi(generics.DestroyAPIView):
    permission_classes = (permissions.AllowAny,)

    queryset = Perks.objects.all()
    serializer_class = PerksSerializer

"""Invoice Model goes here >>>>>>>>>>>>>>>>>>>>>"""

class InvoiceListView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'head', 'post']

    queryset =Invoice.objects.all()
    serializer_class = InvoiceSerializer


class InvoiceDetailView(generics.RetrieveAPIView):
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'head', 'post']

    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

class InvoiceCreateApi(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'head', 'post']

    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

class InvoiceUpdateApi(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.AllowAny,)

    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

class InvoiceDeleteApi(generics.DestroyAPIView):
    permission_classes = (permissions.AllowAny,)

    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

""" Payment Model goes here >>>>>>>>>>>>>>>>>> """


class PaymentListView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'head', 'post']

    queryset =Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentDetailView(generics.RetrieveAPIView):
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'head', 'post']

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class PaymentCreateApi(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'head', 'post']

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class PaymentUpdateApi(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.AllowAny,)

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class PaymentDeleteApi(generics.DestroyAPIView):
    permission_classes = (permissions.AllowAny,)

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

""" Plan Model goes here >>>>>>>>>>>>>>>>>>>>. """

class PlanListView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'head', 'post']

    queryset =Plan.objects.all()
    serializer_class = PlanSerializer


class PlanDetailView(generics.RetrieveAPIView):
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'head', 'post']

    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

class PlanCreateApi(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'head', 'post']

    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

class PlanUpdateApi(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.AllowAny,)

    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

class PlanDeleteApi(generics.DestroyAPIView):
    permission_classes = (permissions.AllowAny,)

    queryset = Plan.objects.all()
    serializer_class = PlanSerializer


"""  Sales Lead goes here """

class SalesLeadListView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'head', 'post']

    queryset =SalesLead.objects.all()
    serializer_class = SalesLeadSerializer


class SalesLeadDetailView(generics.RetrieveAPIView):
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'head', 'post']

    queryset = SalesLead.objects.all()
    serializer_class = SalesLeadSerializer

class SalesLeadCreateApi(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'head', 'post']

    queryset = SalesLead.objects.all()
    serializer_class = SalesLeadSerializer

class SalesLeadUpdateApi(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.AllowAny,)

    queryset = SalesLead.objects.all()
    serializer_class = SalesLeadSerializer

class SalesLeadDeleteApi(generics.DestroyAPIView):
    permission_classes = (permissions.AllowAny,)

    queryset = SalesLead.objects.all()
    serializer_class = SalesLeadSerializer