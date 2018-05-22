from django.db.models import Q
from rest_framework import viewsets
from waldmeister_map.models import UserArea
from waldmeister_map.serializers import AreaSerializer
# DRY Permission package
from dry_rest_permissions.generics import DRYPermissions

# Contains Point
from waldmeister_map.models import Vegetation
from waldmeister_map.serializers import VegetationSerializer
from django.contrib.gis.geos import Point

class UserAreaViewSet(viewsets.ModelViewSet):
    permission_classes = (DRYPermissions,)
    queryset = UserArea.objects.all()

    def get_queryset(self):
        print(self.request.user.is_authenticated)
        print(self.request.user)
        if self.request.user.is_authenticated:
            return UserArea.objects.filter(Q(creator=self.request.user) | Q(public=True))
        return UserArea.objects.filter(public=True)
    serializer_class = AreaSerializer


class VegetationViewSet(viewsets.ModelViewSet):
    queryset = Vegetation.objects.all()

    def get_queryset(self):
        myLng = float(self.request.query_params.get('lat'))
        myLat = float(self.request.query_params.get('lng'))
        pnt_wkt = Point(myLat, myLng)
        print(pnt_wkt)
        # return Vegetation.objects.filter(geom__contains=pnt_wkt)
        return Vegetation.objects.filter(geom__contains=pnt_wkt)

    serializer_class = VegetationSerializer
