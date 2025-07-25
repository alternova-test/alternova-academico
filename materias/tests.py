from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User
from .models import Materia, Nota
from rest_framework_simplejwt.tokens import RefreshToken

# Create your tests here.

class MateriaTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass', rol='profesor')
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

    def test_create_materia(self):
        data = {"nombre": "Matemáticas", "codigo": "MAT101", "profesor": self.user.id}
        response = self.client.post('/api/materias/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
