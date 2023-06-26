import graphene
from graphene_django import DjangoObjectType
from celulares.models import Celular, Vote
from graphql import GraphQLError
from django.db.models import Q




from .models import Celular
from users.schema import UserType


class CelularType(DjangoObjectType):
    class Meta:
        model = Celular

class VoteType(DjangoObjectType):
    class Meta:
        model = Vote

class Query(graphene.ObjectType):
    celulares = graphene.List(CelularType, search=graphene.String())
    votes = graphene.List(VoteType)


    def resolve_celulares(self, info, search=None, **kwargs):
        # The value sent with the search parameter will be in the args variable
        if search:
            filter = (
                Q(precio__icontains=search) |
                Q(color__icontains=search)
            )
            return Celular.objects.filter(filter)

        return Celular.objects.all()
    
    def resolve_votes(self, info, **kwargs):
        return Vote.objects.all()


class CreateCelular(graphene.Mutation):
    id = graphene.Int()
    version = graphene.String()
    descripcion = graphene.String()
    marca = graphene.String()
    precio = graphene.Float()
    tamano = graphene.String()
    sistema = graphene.String()
    fecha = graphene.String()
    color = graphene.String()
    cpu = graphene.String()
    memoria = graphene.String()
    posted_by = graphene.Field(UserType)


    class Arguments:
        version = graphene.String()
        descripcion = graphene.String()
        marca = graphene.String()
        precio = graphene.Float()
        tamano = graphene.String()
        sistema = graphene.String()
        fecha = graphene.String()
        color = graphene.String()
        cpu = graphene.String()
        memoria = graphene.String()

    def mutate(self, info,version,descripcion,marca,precio,tamano,sistema,fecha,color,cpu,memoria):
        user = info.context.user or None
        celula = Celular(
            version=version,
            descripcion=descripcion,
            marca=marca,
            precio=precio,
            tamano=tamano,
            sistema=sistema,
            fecha=fecha,
            color=color,
            cpu=cpu,
            memoria=memoria,
            posted_by=user,
        )
        celula.save()

        return CreateCelular(
            id = celula.id,
            version = celula.version,
            descripcion = celula.descripcion,
            marca = celula.marca,
            precio = celula.precio,
            tamano = celula.tamano,
            sistema = celula.sistema,
            fecha = celula.fecha,
            color = celula.color,
            cpu = celula.cpu,
            memoria = celula.memoria,
            posted_by = celula.posted_by,
        )


class CreateVote(graphene.Mutation):
    user = graphene.Field(UserType)
    celular = graphene.Field(CelularType)

    class Arguments:
        celular_id = graphene.Int()

    def mutate(self, info, celular_id):
        user = info.context.user
        if user.is_anonymous:
            #1
            raise GraphQLError('You must be logged to vote!')

        celular = Celular.objects.filter(id=celular_id).first()
        if not celular:
            #2
            raise Exception('Invalid estrella!')

        Vote.objects.create(
            user=user,
            celular=celular,
        )

        return CreateVote(user=user, celular=celular)

class Mutation(graphene.ObjectType):
    create_celular = CreateCelular.Field()
    create_vote = CreateVote.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
