import graphene import 

import links.schema

class CreateCelulares(graphene.Mutation):
     
     id = graphene.Int()
     url = graphene.String()
     descripcion = graphene.String()
     version = graphene.String()
     descripcion = graphene.String()
     marca = graphene.String()
     precio = graphene.Float()
     sistema = grapheneString()
     fecha = grapheneInt()
     color = grapheneString()
     cpu = grapheneInt()
     memoria = grapheneString()

    #2
    class Arguments:
        url = graphene.String()
        descripcion = graphene.String()

    #3
    def mutate(self, info, descripction, version, description, marca, precio, tamaño, sistema, fecha, color, cpu, memoria):
        
    celular = Celular(
                descripcion=descripcion, 
                version=version, 
                marca=marca, 
                precio=precio, 
                sistema=sistema, 
                fecha=fecha)
        


        celular.save() # insert into Auto()... values (...)

        return CreateCelular(
            id=celular.id,
            url=link.url,
            description=link.description,
        )


#4
class Mutation(graphene.ObjectType):
    create_celular = CreateAuto.Field()

class Query(celulares.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Quer)
