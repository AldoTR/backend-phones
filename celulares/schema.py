import graphene
from graphene_django import DjangoObjectType

from .models import Celular

class CelularType(DjangoObjectType):
    class Meta:
        model = Celular

class Query(graphene.ObjectType):
    celulares = graphene.List(CelularType)

    def resolve_celulares(self, info, **kwargs):
        return Celular.objects.all()
    
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
                    memoria=memoria
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
                             )

class Mutation(graphene.ObjectType):
    create_celular = CreateCelular.Field()
    
schema = graphene.Schema(query=Query, mutation=Mutation)

