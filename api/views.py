from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Note

# Create your views here.

@api_view(['GET'])
def getRoutes(request):

    routes = []

    return Response(routes)
    # return JsonResponse('Our API', safe=False)

@api_view(['GET'])
def getNotes(request):
    notes = Note.object.all()
    return Response('NOTES')

