from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin

from .models import UserArea
# from .models import RegisteredUser


# Register your models here.
admin.site.register(UserArea)
#admin.site.register(RegisteredUser, UserAdmin)