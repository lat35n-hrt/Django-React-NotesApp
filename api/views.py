from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def getRoutes(request):

    routes = []

    return Response(routes)
    # return JsonResponse('Our API', safe=False)

@api_view(['GET'])
def getNotes(request):
    return Response('NOTES')

