from decimal import Decimal

from django.core.management.base import BaseCommand

from propiedades.models import Propiedad

DATOS = [
    ("Casa familiar en Ñuñoa", "CASA", "VENTA", "Av. Irarrázaval 2450", "Santiago", "185000000", 4, 3, "180.00", 1998),
    ("Depto. luminoso cerca del metro", "DEPARTAMENTO", "ALQUILER", "Los Leones 1020", "Providencia", "650000", 2, 1, "58.50", 2015),
    ("Terreno plano con vista", "TERRENO", "VENTA", "Camino El Alba 300", "Lo Barnechea", "95000000", 0, 0, "1200.00", 2005),
    ("Oficina en el centro financiero", "OFICINA", "ALQUILER", "Apoquindo 4500", "Las Condes", "1200000", 0, 2, "90.00", 2018),
]


class Command(BaseCommand):
    help = "Carga propiedades de ejemplo en la base de datos."

    def handle(self, *args, **options):
        creadas = 0
        for t, tipo, op, dire, ciudad, precio, hab, ban, area, anio in DATOS:
            _, nueva = Propiedad.objects.get_or_create(
                direccion=dire, ciudad=ciudad,
                defaults=dict(
                    titulo=t, tipo=tipo, operacion=op, precio=Decimal(precio),
                    habitaciones=hab, banos=ban, area_m2=Decimal(area),
                    anio_construccion=anio, contacto_nombre="Equipo Ventas",
                    contacto_correo="ventas@inmobiliaria.cl",
                    descripcion="Propiedad de ejemplo cargada automáticamente.",
                ),
            )
            creadas += int(nueva)
        self.stdout.write(self.style.SUCCESS(f"Propiedades de ejemplo creadas: {creadas}"))
