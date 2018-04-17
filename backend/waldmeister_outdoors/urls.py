"""waldmeister_outdoors URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.urls import path
from rest_framework import routers
from waldmeister_map.views import index

User = get_user_model()

router = routers.DefaultRouter()

urlpatterns = [
    path(
        'api/',
        include([
            path('admin/', admin.site.urls),
            path('waldmeister-map/', include('waldmeister_map.urls')),
            url(r'^$', index, name='index'),

            # Rest Framework
            url(r'^', include(router.urls)),
            url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework_auth')),
        ])
     )
]
