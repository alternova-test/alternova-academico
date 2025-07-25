# Aternova Académico

Sistema académico con Django y Django REST Framework. Permite la gestión de usuarios (administradores, profesores y estudiantes), materias, notas, reportes y notificaciones.

---

## 🛠 Tecnologías utilizadas

- Python 3.13.5
- Django 4.x
- Django REST Framework
- Simple JWT (Autenticación)
- SQLite (por defecto)
- Postman (prueba de API)

---

## 🚀 Instalación

1. **Clonar el repositorio:**

```bash
git clone https://github.com/alternova-test/alternova-academico.git
cd alternova-academico
```
2. **crear entorno virtual:"

```bash
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate
```

3. **Instalar dependencias:**

```bash
pip install -r requirements.txt
```

4. **Aplicar migraciones:**

```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Crear superusuario:**

```bash
python manage.py createsuperuser
```

6. **Levantar servidor:**

```bash
python manage.py runserver
```

## Pruebas

Realizar con herramineta Postman o Insomnia con Authorization: Bearer Token
- POST /api/token/ → Obtener token
Body:{
  "username": "usuario",
  "password": "contraseña"
}
- POST /api/token/refresh/ → Renovar token
- Body:{
  "refresh": "token_refresh"
}
- GET /api/materias/ → Listar naterias
- POST /api/materias/ → Crear materias 
Body:{
  "nombre": "",
  "codigo": "",
  "profesor": 2
}
- GET /api/materias/<id>/ →  Obtener detalle de una materia
- PUT /api/materias/<id>/ →  Actualizar una materia
- DELETE /api/materias/<id>/ →  Eliminar una materia
- GET /api/notas/  →  Listar notas
- POST /api/notas/  →  Crear nota
- Body:{
  "estudiante": 3,
  "materia": 1,
  "nota": 4.5
}
- GET /api/notas/<id>/  →  Obtener nota específica
- PUT /api/notas/<id>/  →  Actualizar nota
- DELETE /api/notas/<id>/  →  Eliminar nota
- GET /api/reportes/promedio/<estudiante_id>/  →  Promedio por estudiante
- GET /api/notificaciones/  →  Listar notificaciones
- POST /api/notificaciones/  →  Crear notificación
Body:{
  "usuario": 3,
  "mensaje": "Tienes una nueva nota"
}
- GET /api/notificaciones/<id>/  →  Ver detalle
- PUT /api/notificaciones/<id>/  →  Actualizar notificación
Body:{
  "leido": true
}
- DELETE /api/notificaciones/<id>/  →  Eliminar notificación

Se comparte vía email colección de endpoints de endpoints principales en Postman.
Todos los endpoints deben utilizar Bearer Token, a escepción del login.

Opcional: python manage.py test

<img width="1530" height="1022" alt="image" src="https://github.com/user-attachments/assets/d4bc33f5-84bc-45c4-a34c-fceb8fc91a27" />
<img width="1527" height="1030" alt="image" src="https://github.com/user-attachments/assets/81b250f9-2395-4d33-a6ca-e18ea6a885fe" />

## Swagger

Correr el proyecto: python manage.py runserver
Desde el navegador ingresar a: http://localhost:8000/api/docs/





