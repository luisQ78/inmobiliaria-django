from datetime import date
from decimal import Decimal

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models


def validar_anio(valor):
    """El año de construcción debe estar entre 1900 y el año actual."""
    actual = date.today().year
    if valor < 1900 or valor > actual:
        raise ValidationError(f"El año debe estar entre 1900 y {actual}.")


class Propiedad(models.Model):
    TIPOS = [
        ("CASA", "Casa"),
        ("DEPARTAMENTO", "Departamento"),
        ("TERRENO", "Terreno"),
        ("OFICINA", "Oficina"),
        ("LOCAL", "Local comercial"),
    ]
    OPERACIONES = [
        ("VENTA", "Venta"),
        ("ALQUILER", "Alquiler"),
    ]
    ESTADOS = [
        ("DISPONIBLE", "Disponible"),
        ("RESERVADA", "Reservada"),
        ("VENDIDA", "Vendida"),
        ("ALQUILADA", "Alquilada"),
    ]

    titulo = models.CharField("Título", max_length=120)
    tipo = models.CharField("Tipo de propiedad", max_length=20, choices=TIPOS)
    operacion = models.CharField("Operación", max_length=10, choices=OPERACIONES)
    direccion = models.CharField("Dirección", max_length=200)
    ciudad = models.CharField("Ciudad", max_length=80)
    precio = models.DecimalField(
        "Precio", max_digits=12, decimal_places=2,
        validators=[MinValueValidator(Decimal("0.01"), "El precio debe ser mayor que cero.")],
    )
    habitaciones = models.PositiveSmallIntegerField("Habitaciones", default=0)
    banos = models.PositiveSmallIntegerField("Baños", default=0)
    area_m2 = models.DecimalField(
        "Área (m²)", max_digits=8, decimal_places=2,
        validators=[MinValueValidator(Decimal("0.01"), "El área debe ser mayor que cero.")],
    )
    anio_construccion = models.PositiveSmallIntegerField(
        "Año de construcción", validators=[validar_anio]
    )
    estado = models.CharField("Estado", max_length=12, choices=ESTADOS, default="DISPONIBLE")
    descripcion = models.TextField("Descripción", blank=True)
    contacto_nombre = models.CharField("Nombre de contacto", max_length=100)
    contacto_correo = models.EmailField("Correo de contacto")
    fecha_registro = models.DateTimeField("Fecha de registro", auto_now_add=True)

    class Meta:
        db_table = "propiedad"
        ordering = ["-fecha_registro"]
        verbose_name = "propiedad"
        verbose_name_plural = "propiedades"

    def __str__(self):
        return f"{self.titulo} - {self.ciudad}"
