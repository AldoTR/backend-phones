from django.test import TestCase
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
CREATE_CELULAR_MUTATION = '''
 mutation createCelularMutation($version: String, $description: String, $marca: String, $precio: Int, $tamano: String, $sistema: String, $fecha: String, $color: String, $cpu: String, $memoria: String) {
     createCelular(version: $version, descripcion: $descripcion, marca: $marca, precio: $precio, tamano: $tamano, sistema: $sistema, fecha: $fecha, color: $color, cpu: $cpu, memoria: $memoria) {
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
            CELULARES_QUERY
        )
        
        content = json.loads(response.content)
        #print(content)
        self.assertResponseNoErrors(response)
        print("query celulares results")
        print (content)
        assert len(content['data']['celulares']) == 2

def test_createCelular_mutation(self):
      
        response = self.query(
            CREATE_CELULAR_MUTATION,
            variables={'version': '14 Pro Max', 'descripcion': 'Celular de Apple', 'marca': 'Apple', 'precio': '30000', 'tamano': 'Normal', 'sistema': 'iOS', 'fecha': 'Septiembre de 2022', 'color': 'Blanco', 'cpu': '8GB', 'memoria': '256 GB'}
        )
        print('mutation ')
        print(response)
        content = json.loads(response.content)
        print(content)
        self.assertResponseNoErrors(response)
        self.assertDictEqual({"createCelular" : {"version: 14 Pro Max"}}, content['data'])
