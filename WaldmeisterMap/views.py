from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

#Serializers
#from django.contrib.auth.models import User, Group
from WaldmeisterMap.serializers import AreaSerializer
from WaldmeisterMap.models import UserArea
#from WaldmeisterMap.serializers import RegisteredUserSerializer


#Django rest framework
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from django.contrib.auth import get_user_model
User = get_user_model()



# ARCHIVE
# Create your views here.
# def index(request):
# 	return HttpResponse("<h1> WaldmeisterMap</h1>")


#Register return
# @csrf_exempt
# def register(request):
# 	if request.method == 'POST':
# 	    serializer = RegisteredUserSerializer(request.data)
# 	    if serializer.is_valid():
# 	        serializer.save()
# 	        return Response(serializer.data)
# 	    else:
# 	    	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #return Response(request.body)
    
    # data = JSONParser().parse(request)
    # serializer = RegisteredUserSerializer(data=data)
    # if serializer.is_valid():
    #     serializer.save()
    #     return JSONResponse(serializer.data, status=201)
    # return JSONResponse(serializer.errors, status=400)

#Render index template
def index(request):
    context = {
        'days': [1, 2, 3, 4],
    }
    return render(request, 'map.html', context)


# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer


# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer

# class UserAreaViewSet(viewsets.ModelViewSet):
#     queryset = UserArea.objects.all()
#     def get_queryset(self):
#         if

class UserAreaViewSet(viewsets.ModelViewSet):
    queryset = UserArea.objects.all()
    def get_queryset(self):	
        print(self.request.user.is_authenticated)
        print(self.request.user)
        if (self.request.user.is_authenticated):
            #return UserArea.objects.filter(creator = self.request.user | public = True)
            return UserArea.objects.filter( Q(creator=self.request.user) | Q(public=True) )
        else:
            return UserArea.objects.filter(public = True)
        return None
    serializer_class = AreaSerializer



