import graphene 

import celulares.schema

class Query(celulares.schema.Query, graphene.ObjectType):
    pass

class Mutation(celulares.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)