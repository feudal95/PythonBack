from rest_framework import serializers

from app1.models import Person, Job

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
        #__all__ usa todos los campos

class JobSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Job
        fields = '__all__'

class SecondJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        field = ('id', 'name')

class MySerializer(serializers.Serializers):
    first_name = serializers.CharField(max_length = 32)
    last_name = serializers.CharField(max_length = 32)
    namme = serializers.CharField(max_length = 32)
    age = serializers.IntegerField()