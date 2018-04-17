from django.contrib.gis.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class UserArea(models.Model):
    label = models.CharField(max_length=50)
    public = models.BooleanField()
    polygon = models.MultiPolygonField(4326)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('creator',)
