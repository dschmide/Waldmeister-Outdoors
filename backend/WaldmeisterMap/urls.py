#urls.py in WaldmeisterMap

from django.conf.urls import url, include
from rest_framework import routers
#from WaldmeisterMap import views
from . import views

#JWT Token
from rest_framework_jwt.views import obtain_jwt_token

#Djoser
from django.urls import include, re_path

#Swagger
from rest_framework_swagger.views import get_swagger_view



router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)
#router.register(r'register', views.register)
router.register(r'areas', views.UserAreaViewSet)

#swagger
schema_view = get_swagger_view(title='Waldmeister API')


urlpatterns = [
	#/WaldmeisterMap/
    url(r'^$', views.index, name='index'),

    #Rest test
	url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #WaldmeisterMap/map
    #url(r'^/Map/', views.map, name='map')

    #url(r'^register', views.register, name='register'),

    #url(r'^rest-auth/', include('rest_auth.urls')),
	#JWT Token
    #url(r'^api-token-auth/', obtain_jwt_token),

    #Djoser
    #re_path(r'^api/', include('djoser.urls')),
    url(r'^auth/', include('djoser.urls')),
    url(r'^auth/', include('djoser.urls.authtoken')),
    url(r'^auth/', include('djoser.urls.jwt')),
    
    #swagger
    url(r'^swagger', schema_view)
]