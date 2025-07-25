from rest_framework import serializers
from .models import Materia, Nota

class MateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materia
        fields = '__all__'

class NotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nota
        fields = '__all__'