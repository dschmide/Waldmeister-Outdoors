from django.conf.urls import url
from django.urls import include
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from . import views

router = routers.DefaultRouter()
router.register(r'areas', views.UserAreaViewSet)

schema_view = get_swagger_view(title='Waldmeister API')


urlpatterns = [
    # Rest api
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^auth/', include('djoser.urls')),
    url(r'^auth/', include('djoser.urls.authtoken')),
    url(r'^auth/', include('djoser.urls.jwt')),

    # swagger
    url(r'^swagger', schema_view)
]
