from django.db import models
from django.contrib.gis.db import models
#from django.contrib.gis import geos

#Create Extension
from django.contrib.postgres.operations import CreateExtension
from django.db import migrations

#Djoser
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
import uuid

from django.contrib.auth import get_user_model
User = get_user_model()


# class Migration(migrations.Migration):

#     operations = [
#         CreateExtension('postgis'),
#     ]

# Create your models here.

# class RegisteredUser(AbstractBaseUser):
# 	username = models.CharField(max_length=50, unique=True)
# 	password = models.CharField(max_length=50)
# 	displayname = models.CharField(max_length=50, unique=True)
# 	USERNAME_FIELD = 'displayname'
# 	class Meta:
# 		ordering = ('username',)


class UserArea(models.Model):
	label = models.CharField(max_length=50)
	public = models.BooleanField()
	polygon = models.MultiPolygonField(4326)
	creator = models.ForeignKey(User, on_delete=models.CASCADE)
	class Meta:
		ordering = ('creator',)

