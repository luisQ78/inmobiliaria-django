# Inmobiliaria / Propiedad — Django + MySQL/MariaDB (XAMPP)

CRUD completo de propiedades (venta/alquiler). Sin login ni registro de usuarios.

## 1. Puesta en marcha

1. Abre **XAMPP** y arranca **Apache** y **MySQL**.
2. En phpMyAdmin (http://localhost/phpmyadmin) crea la base de datos:
   ```sql
   CREATE DATABASE inmobiliaria_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   ```
3. En la carpeta del proyecto:
   ```bash
   python -m venv venv
   venv\Scripts\activate          # Windows  (Linux/Mac: source venv/bin/activate)
   pip install -r requirements.txt
   python manage.py makemigrations propiedades
   python manage.py migrate
   python manage.py cargar_datos   # opcional: datos de ejemplo
   python manage.py runserver
   ```
4. Abre http://127.0.0.1:8000/

Si tu MySQL tiene contraseña o usa otro puerto, cámbialo en `inmobiliaria_project/settings.py` (`DATABASES`).
Se usa Django 4.2 LTS porque es compatible con el MariaDB 10.4 que traen muchas versiones de XAMPP.

## 2. Qué cumple de la pauta

| Requisito | Dónde |
|---|---|
| models / views / urls / templates / formularios | `propiedades/` |
| Formularios de crear y editar **distintos** | `PropiedadCrearForm` (sin estado) y `PropiedadEditarForm` (con estado) en `forms.py`; templates `crear.html` y `editar.html` |
| Validaciones | `models.py` (precio > 0, área > 0, año 1900–actual, correo) y `forms.py` (título mínimo, habitaciones/baños, dirección duplicada) |
| Listado, detalle, eliminar con confirmación | `lista.html`, `detalle.html`, `eliminar.html` |
| CRUD a nivel de base de datos | `docs/crud_mysql_demo.sql` (INSERT/SELECT/UPDATE/DELETE en phpMyAdmin) |
| Migraciones | `makemigrations` genera `propiedades/migrations/0001_initial.py` (súbela a Git) |

## 3. Git / GitHub: participación individual

Este .zip **no trae historial de Git**: cada integrante debe hacer sus propios commits. Sugerencia de reparto:

- **Integrante A** — rama `feature/modelo-formularios`: `models.py`, `forms.py` (validaciones), vistas y templates de **crear** y **editar**, migraciones.
- **Integrante B** — rama `feature/listado-navegacion`: `base.html`, `home.html`, `lista.html` (búsqueda/filtros), `detalle.html`, **eliminar**, estilos, `cargar_datos`, SQL de demostración.

```bash
git init
git add . && git commit -m "Estructura inicial del proyecto"      # solo uno hace esto
git branch -M main
git remote add origin https://github.com/USUARIO/REPO.git
git push -u origin main

# cada integrante, en su máquina:
git checkout -b feature/su-rama
# ...trabaja, y commitea seguido con mensajes claros...
git add archivo && git commit -m "Agrega validación de precio"
git push -u origin feature/su-rama
# luego abre un Pull Request hacia main en GitHub
```

Para la defensa individual, cada uno debe poder explicar **todo** el flujo (modelo → migración → formulario → vista → URL → template), no solo su parte.
