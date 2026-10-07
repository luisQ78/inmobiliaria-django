from django.urls import path

from . import views

app_name = "propiedades"

urlpatterns = [
    path("", views.home, name="home"),
    path("propiedades/", views.lista, name="lista"),
    path("propiedades/nueva/", views.crear, name="crear"),
    path("propiedades/<int:pk>/", views.detalle, name="detalle"),
    path("propiedades/<int:pk>/editar/", views.editar, name="editar"),
    path("propiedades/<int:pk>/eliminar/", views.eliminar, name="eliminar"),
]
