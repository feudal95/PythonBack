#from django.shortcuts import render
import imp
from os import stat
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from app1.serializers import PersonSerializer
from app1.models import Person

#@api_view(['GET'])#aqui se indica como va a recibir los datos
def hello(request, name):
    return Response({'message':f'Hello {name} world'}, status=status.HTTP_200_OK)

class PersonListAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        person_list = Person.objects.all()
        #                #cuado se manda a llamar el objeto Objects que permite llamar a la base de datos y manipular los dtos que existan
        serializers = PersonSerializer(person_list, many=True)
        #                                           #cuando usas el 'many' le indicas al codigo que vamos a serializar muchos objetos, por default serialzia solo uno

        return Response(serializers.data, status=status.HTTP_200_OK)
        #               serializer. data. transforma la respuesta en JSON

class PersonCreateAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    #se define la funcion con el metodo que se va a utilizar
        #return Response({'message':'another view'})
# Create your views here.
