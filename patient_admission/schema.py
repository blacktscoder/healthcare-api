import graphene
from graphene_django.types import DjangoObjectType
from .models import Patient

class PatientType(DjangoObjectType):
    class Meta:
        model = Patient
        fields = "__all__"

class Query(graphene.ObjectType):
    all_patients = graphene.List(PatientType)
    patient = graphene.Field(PatientType, id=graphene.Int(required=True))

    def resolve_all_patients(self, info, **kwargs):
        return Patient.objects.all()

    def resolve_patient(self, info, id):
        return Patient.objects.get(pk=id)

class CreatePatient(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        age = graphene.Int(required=True)
        gender = graphene.String(required=True)

    patient = graphene.Field(PatientType)

    def mutate(self, info, name, age, gender):
        patient = Patient.objects.create(name=name, age=age, gender=gender)
        return CreatePatient(patient=patient)

class UpdatePatient(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String()
        age = graphene.Int()
        gender = graphene.String()

    patient = graphene.Field(PatientType)

    def mutate(self, info, id, name=None, age=None, gender=None):
        patient = Patient.objects.get(pk=id)
        if name:
            patient.name = name
        if age:
            patient.age = age
        if gender:
            patient.gender = gender
        patient.save()
        return UpdatePatient(patient=patient)

class DeletePatient(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    patient = graphene.Field(PatientType)

    def mutate(self, info, id):
        patient = Patient.objects.get(pk=id)
        patient.delete()
        return DeletePatient(patient=None)

class Mutation(graphene.ObjectType):
    create_patient = CreatePatient.Field()
    update_patient = UpdatePatient.Field()
    delete_patient = DeletePatient.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
