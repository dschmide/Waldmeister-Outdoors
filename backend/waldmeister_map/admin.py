from django.contrib import admin
from .models import UserArea
from .models import Vegetation

# Register a Django DB Model
admin.site.register(UserArea)
admin.site.register(Vegetation)
