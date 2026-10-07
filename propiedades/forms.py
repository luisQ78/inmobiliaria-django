from django import forms

from .models import Propiedad


class BootstrapMixin:
    """Agrega clases de Bootstrap a todos los campos."""

    def _aplicar_bootstrap(self):
        for nombre, campo in self.fields.items():
            if isinstance(campo.widget, forms.Select):
                campo.widget.attrs["class"] = "form-select"
            else:
                campo.widget.attrs["class"] = "form-control"


class ValidacionesPropiedad:
    """Validaciones compartidas entre el formulario de crear y el de editar."""

    def clean_titulo(self):
        titulo = self.cleaned_data["titulo"].strip()
        if len(titulo) < 5:
            raise forms.ValidationError("El título debe tener al menos 5 caracteres.")
        return titulo

    def clean_precio(self):
        precio = self.cleaned_data["precio"]
        if precio <= 0:
            raise forms.ValidationError("El precio debe ser mayor que cero.")
        return precio

    def clean_area_m2(self):
        area = self.cleaned_data["area_m2"]
        if area <= 0:
            raise forms.ValidationError("El área debe ser mayor que cero.")
        return area

    def clean_habitaciones(self):
        valor = self.cleaned_data["habitaciones"]
        if valor > 50:
            raise forms.ValidationError("Cantidad de habitaciones no realista (máximo 50).")
        return valor

    def clean_banos(self):
        valor = self.cleaned_data["banos"]
        if valor > 50:
            raise forms.ValidationError("Cantidad de baños no realista (máximo 50).")
        return valor

    def clean(self):
        datos = super().clean()
        direccion = (datos.get("direccion") or "").strip()
        ciudad = (datos.get("ciudad") or "").strip()
        if direccion and ciudad:
            existentes = Propiedad.objects.filter(
                direccion__iexact=direccion, ciudad__iexact=ciudad
            )
            if self.instance.pk:
                existentes = existentes.exclude(pk=self.instance.pk)
            if existentes.exists():
                raise forms.ValidationError(
                    "Ya existe una propiedad registrada con esa dirección en esa ciudad."
                )
        return datos


class PropiedadCrearForm(ValidacionesPropiedad, BootstrapMixin, forms.ModelForm):
    """Formulario de CREACIÓN: no pide el estado (se crea como 'Disponible')."""

    class Meta:
        model = Propiedad
        exclude = ["estado", "fecha_registro"]
        widgets = {"descripcion": forms.Textarea(attrs={"rows": 3})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._aplicar_bootstrap()


class PropiedadEditarForm(ValidacionesPropiedad, BootstrapMixin, forms.ModelForm):
    """Formulario de EDICIÓN: incluye el estado y permite cambiarlo."""

    class Meta:
        model = Propiedad
        exclude = ["fecha_registro"]
        widgets = {"descripcion": forms.Textarea(attrs={"rows": 4})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._aplicar_bootstrap()
