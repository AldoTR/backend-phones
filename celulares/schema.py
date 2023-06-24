import graphene
from graphene_django import DjangoObjectType
from users.schema import UserType
from graphql import GraphQLError
from django.db.models import Q
from .models import Celular, Vote


class CelularType(DjangoObjectType):
    class Meta:
        model = Celular
        
class VoteType(DjangoObjectType):
    class Meta:
        model = Vote        

class Query(graphene.ObjectType):
    celulares = graphene.List(CelularType)
    votes = graphene.List(VoteType)

    def resolve_celulares(self, info, search=None, **kwargs):
        if search:
            filter = (
                Q(marca__icontains=search) |
                Q(posted_by__icontains=search)
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
    #2
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
    #3
    def mutate(self, info, version, descripcion, marca, precio, tamano, sistema, fecha, color, cpu, memoria):
        user = info.context.user or None

        celular = Celular(
                    descripcion=descripcion,
                    version=version,
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
        celular.save()
        
        return CreateCelular(
                id=celular.id,
                descripcion=celular.descripcion,
                version=celular.version,
                marca=celular.marca,
                precio=celular.precio,
                tamano=celular.tamano,
                sistema=celular.sistema,
                fecha=celular.fecha,
                color=celular.color,
                cpu=celular.cpu,
                memoria=celular.memoria,
                posted_by=celular.posted_by,
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
            raise Exception('Invalid celular!')

        Vote.objects.create(
            user=user,
            celular=celular,
        )

        return CreateVote(user=user, celular=celular)

class Mutation(graphene.ObjectType):
    create_celular = CreateCelular.Field()
    create_vote = CreateVote.Field()
    
schema = graphene.Schema(query=Query, mutation=Mutation)

