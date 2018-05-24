from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.urls import path
from rest_framework import routers

User = get_user_model()

router = routers.DefaultRouter()

urlpatterns = [
    path(
        'api/',
        include([
            path('admin/', admin.site.urls),
            path('waldmeister-map/', include('restful_api.urls')),
            # Rest Framework
            url(r'^', include(router.urls)),
            url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework_auth')),  # noqa
        ])
     )
]
