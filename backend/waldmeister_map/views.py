from django.db.models import Q
from django.shortcuts import render
from rest_framework import viewsets
from waldmeister_map.models import UserArea
from waldmeister_map.serializers import AreaSerializer


def index(request):
    context = {
        'days': [1, 2, 3, 4],
    }
    return render(request, 'map.html', context)


class UserAreaViewSet(viewsets.ModelViewSet):
    queryset = UserArea.objects.all()

    def get_queryset(self):
        print(self.request.user.is_authenticated)
        print(self.request.user)
        if self.request.user.is_authenticated:
            return UserArea.objects.filter(Q(creator=self.request.user) | Q(public=True))
        return UserArea.objects.filter(public=True)
    serializer_class = AreaSerializer
