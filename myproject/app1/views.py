#from django.shortcuts import render
import imp
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from app1.serializers import PersonSerializer
#@api_view(['GET'])#aqui se indica como va a recibir los datos
def hello(request, name):
    return Response({'message':f'Hello {name} world'}, status=status.HTTP_200_OK)

class ClaseUnoApiView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
    #se define la funcion con el metodo que se va a utilizar
        return Response({'message':'another view'})
# Create your views here.
