from rest_framework import viewsets, permissions
from .models import Notificacion
from .serializers import NotificacionSerializer

# Create your views here.

class NotificacionViewSet(viewsets.ModelViewSet):
    queryset = Notificacion.objects.all()
    serializer_class = NotificacionSerializer
    permission_classes = [permissions.IsAuthenticated]