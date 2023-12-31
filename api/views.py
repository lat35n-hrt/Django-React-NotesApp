from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Note
from .serializers import NoteSerializer

# Create your views here.

@api_view(['GET'])
def getRoutes(request):

    routes = []

    return Response(routes)
    # return JsonResponse('Our API', safe=False)

@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all()
    note_serializer = NoteSerializer(notes, many=True)
    return Response(note_serializer.data)

@api_view(['GET'])
def getNote(request, pk):
    notes = Note.objects.get(id=pk)
    note_serializer = NoteSerializer(notes, many=False)
    return Response(note_serializer.data)


@api_view(['POST'])
def createNote(request):
    data = request.data 
    note = Note.objects.create(
        body=data['body']
    )
    return Response


@api_view(['PUT'])
def updateNote(request, pk):
    data = request.data
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(instance=note, data=data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteNote(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response('Note was deleted')


