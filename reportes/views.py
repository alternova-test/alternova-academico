from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from materias.models import Nota
from django.db import models

# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def promedio_estudiante(request, estudiante_id):
    notas = Nota.objects.filter(estudiante_id=estudiante_id)
    promedio = notas.aggregate(models.Avg('nota'))['nota__avg'] or 0
    return Response({'estudiante_id': estudiante_id, 'promedio': promedio})