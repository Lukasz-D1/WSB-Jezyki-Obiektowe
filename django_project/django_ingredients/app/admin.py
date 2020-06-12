from django.contrib import admin
from django.contrib.auth.models import Permission
from app.models import *

admin.site.register(Ingredient)
admin.site.register(Type)
admin.site.register(Nutrients)
admin.site.register(Permission)
