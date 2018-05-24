from django.db.models import Q
from rest_framework import viewsets
from waldmeister_map.models import UserArea
from waldmeister_map.serializers import AreaSerializer
# DRY Permission package
from dry_rest_permissions.generics import DRYPermissions

# Contains Point
from waldmeister_map.models import Vegetation
from waldmeister_map.serializers import VegetationSerializer

from django.contrib.gis.geos import Polygon
from django.contrib.gis.geos import Point


class UserAreaViewSet(viewsets.ModelViewSet):
    permission_classes = (DRYPermissions,)
    queryset = UserArea.objects.all()

    def get_queryset(self):
        print(self.request.user.is_authenticated)
        print(self.request.user)
        if self.request.user.is_authenticated:
            return UserArea.objects.filter(Q(creator=self.request.user) | Q(public=True))  # noqa
        return UserArea.objects.filter(public=True)
    serializer_class = AreaSerializer
    http_method_names = ['get', 'put', 'delete', 'post']


class VegetationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Vegetation.objects.all()

    def get_queryset(self):
        myLat = float(self.request.query_params.get('lat'))
        myLng = float(self.request.query_params.get('lng'))
        pnt_wkt = Point(myLat, myLng)
        print(pnt_wkt.geom_typeid)

        ne = (myLat + 0.00000001, myLng + 0.00000001)
        sw = (myLat - 0.00000001, myLng - 0.00000001)

        xmin = sw[1]
        ymin = sw[0]
        xmax = ne[1]
        ymax = ne[0]
        bbox = (xmin, ymin, xmax, ymax)

        boundingbox = Polygon.from_bbox(bbox)
        print(boundingbox.geom_typeid)
        return Vegetation.objects.filter(geom__contains=boundingbox)

        # return Vegetation.objects.filter(geom__intersects=pnt_wkt)
        # return Vegetation.objects.all()
        # return Vegetation.objects.all()[:5]

    serializer_class = VegetationSerializer
