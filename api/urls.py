from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('api/notes/', views.getNotes, name="notes"),
    path('api/notes/create', views.createNote, name="create-note"),
    path('api/notes/<str:pk>/update', views.updateNote, name="update-note"),
    path('api/notes/<str:pk>/delete', views.deleteNote, name="delete-note"),
    path('api/notes/<str:pk>/', views.getNote, name="note"),
]
