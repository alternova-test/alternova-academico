from django.db import models
from users.models import User

# Create your models here.

class Materia(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20, unique=True)
    profesor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, limit_choices_to={'rol': 'profesor'})

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"
    


class Nota(models.Model):
    estudiante = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'rol': 'estudiante'})
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        unique_together = ('estudiante', 'materia')

    def __str__(self):
        return f"{self.estudiante.username} - {self.materia.nombre} - {self.nota}"