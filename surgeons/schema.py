import graphene
from graphene_django import DjangoObjectType
from .models import Surgeon

class SurgeonType(DjangoObjectType):
    class Meta:
        model = Surgeon
        fields = "__all__"

class Query(graphene.ObjectType):
    all_surgeons = graphene.List(SurgeonType)
    surgeon = graphene.Field(SurgeonType, id=graphene.Int(required=True))

def resolve_all_surgeons(self,info):
    return Surgeon.objects.all()

def resolve_surgeon(self,info,id):
    return Surgeon.objects.get(pk=id)

class CreateSurgeon(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        specialisation = graphene.String(required=True)
        email = graphene.String(required=True)
surgeon = graphene.Field(SurgeonType)

def mutate(self, info, name, specialisation, email):
    surgeon = Surgeon.obejcts.create(
        name=name,
        specialisation=specialisation,
        email=email
    )
    return CreateSurgeon(surgeon=surgeon)

class Mutation(graphene.ObjectType):
    create_surgeon = CreateSurgeon.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)