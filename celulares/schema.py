import graphene
from graphene_django import DjangoObjectType

from .models import Celular

class CelularType(DjangoObjectType):
    class Meta:
        model = Celular

class Query(graphene.ObjectType):
    links = graphene.List(LinkType)

    def resolve_links(self, info **kwargs):
        return Link.objects.all()
