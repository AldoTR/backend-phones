import graphene 
import users.schema
import celulares.schema
import consultas.schema

import graphql_jwt

class Query(consultas.schema.Query,users.schema.Query, celulares.schema.Query, graphene.ObjectType):
    pass

class Mutation(consultas.schema.Mutation,users.schema.Mutation, celulares.schema.Mutation, graphene.ObjectType): 
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)