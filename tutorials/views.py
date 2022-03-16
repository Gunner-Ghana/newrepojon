from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from tutorials.models import AccountMove
from tutorials.serialize import TutorialSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'DELETE'])
def tutorial_list(request):
    # GET list of tutorials, POST a new tutorial, DELETE all tutorials
       if request.method == 'GET':
        accountMove = AccountMove.objects.all().values('id','name','date','narration')
        
        #title = request.GET.get('title', None)
        #if title is not None:
         #   tutorials = tutorials.filter(title__icontains=title)
        
        tutorials_serializer = TutorialSerializer(accountMove, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)

       elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = TutorialSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def tutorial_detail(request, pk):
    # find tutorial by pk (id)
    try: 
        accountMove = AccountMove.objects.filter(id=pk).values('id','name','date','narration')
        tutorials_serializer = TutorialSerializer(accountMove, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
    except AccountMove.DoesNotExist: 
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    # GET / PUT / DELETE tutorial

