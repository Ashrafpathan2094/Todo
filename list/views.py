from list.models import Lists
from list.serializers import ListsSerializer





from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.



class TodosView(APIView):
    
    def get(self,request):
        todos = Lists.objects.filter(owner=request.user.id)
        serializer = ListsSerializer(todos, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = ListsSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
        
        else:
            data = serializer.data
            owner =request.user
            get_data = Lists(owner= owner, title = data['title'],description= data['description'],done = False)
            get_data.save()
            request.data['id'] = get_data.pk
            return Response(request.data,status= status.HTTP_201_CREATED)
        