from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PropiedadCrearForm, PropiedadEditarForm
from .models import Propiedad


def home(request):
    contexto = {
        "total": Propiedad.objects.count(),
        "disponibles": Propiedad.objects.filter(estado="DISPONIBLE").count(),
        "recientes": Propiedad.objects.all()[:3],
    }
    return render(request, "propiedades/home.html", contexto)


def lista(request):
    propiedades = Propiedad.objects.all()
    q = request.GET.get("q", "").strip()
    tipo = request.GET.get("tipo", "")
    operacion = request.GET.get("operacion", "")

    if q:
        propiedades = propiedades.filter(
            Q(titulo__icontains=q) | Q(ciudad__icontains=q) | Q(direccion__icontains=q)
        )
    if tipo:
        propiedades = propiedades.filter(tipo=tipo)
    if operacion:
        propiedades = propiedades.filter(operacion=operacion)

    contexto = {
        "propiedades": propiedades,
        "q": q,
        "tipo": tipo,
        "operacion": operacion,
        "tipos": Propiedad.TIPOS,
        "operaciones": Propiedad.OPERACIONES,
    }
    return render(request, "propiedades/lista.html", contexto)


def detalle(request, pk):
    propiedad = get_object_or_404(Propiedad, pk=pk)
    return render(request, "propiedades/detalle.html", {"propiedad": propiedad})


def crear(request):
    if request.method == "POST":
        form = PropiedadCrearForm(request.POST)
        if form.is_valid():
            propiedad = form.save()
            messages.success(request, f"Propiedad «{propiedad.titulo}» creada correctamente.")
            return redirect("propiedades:lista")
    else:
        form = PropiedadCrearForm()
    return render(request, "propiedades/crear.html", {"form": form})


def editar(request, pk):
    propiedad = get_object_or_404(Propiedad, pk=pk)
    if request.method == "POST":
        form = PropiedadEditarForm(request.POST, instance=propiedad)
        if form.is_valid():
            form.save()
            messages.success(request, f"Propiedad «{propiedad.titulo}» actualizada correctamente.")
            return redirect("propiedades:detalle", pk=propiedad.pk)
    else:
        form = PropiedadEditarForm(instance=propiedad)
    return render(request, "propiedades/editar.html", {"form": form, "propiedad": propiedad})


def eliminar(request, pk):
    propiedad = get_object_or_404(Propiedad, pk=pk)
    if request.method == "POST":
        titulo = propiedad.titulo
        propiedad.delete()
        messages.success(request, f"Propiedad «{titulo}» eliminada.")
        return redirect("propiedades:lista")
    return render(request, "propiedades/eliminar.html", {"propiedad": propiedad})
