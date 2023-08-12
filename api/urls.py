from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('api/notes/', views.getNotes, name="notes"),
    path('api/notes/<str:pk>', views.getNote, name="note"),
]
