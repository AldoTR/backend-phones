from django.test import TestCase

# Create your tests here.

from graphene_django.utils.testing import GraphQLTestCase
from mixer.backend.django import mixer
import graphene
import json

# Create your tests here.
from celulares.schema import schema
from celulares.models import Celular

CELULARES_QUERY = '''
 {
   celulares {
     id
     version
     descripcion
     marca
     precio
     tamano
     sistema
     fecha
     color
     cpu
     memoria
   }
 }
'''
class CelularTestCase(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema
    def setUp(self):
       self.celular1 = mixer.blend(Celular)
       self.celular2 = mixer.blend(Celular)
        
    def test_celulares_query(self):
        response = self.query(
            CELULARES_QUERY,
        )
        
        content = json.loads(response.content)
        #print(content)
        self.assertResponseNoErrors(response)
        print("query celulares results ")
        print (content)
        assert len(content['data']['celulares']) == 2
