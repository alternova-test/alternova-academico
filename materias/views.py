from rest_framework import viewsets, permissions
from .models import Materia, Nota
from .serializers import MateriaSerializer, NotaSerializer
from django.shortcuts import render

# Create your views here.

class MateriaViewSet(viewsets.ModelViewSet):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer
    permission_classes = [permissions.IsAuthenticated]

class NotaViewSet(viewsets.ModelViewSet):
    queryset = Nota.objects.all()
    serializer_class = NotaSerializer
    permission_classes = [permissions.IsAuthenticated]
