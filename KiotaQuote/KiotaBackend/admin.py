from django.contrib import admin

# Register your models here.
from .models import Users
from .models import Inventory
from .models import Shops

admin.site.register(Users)
admin.site.register(Inventory)
admin.site.register(Shops)
