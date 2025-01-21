from django.contrib import admin
from .models import CustomUser 

# Give me Admin page for adding Bracnh and Role
admin.site.register(CustomUser)