from django.contrib import admin
from .models import CustomUser , Branch , Role , File , Tippani

# Give me Admin page for adding Bracnh and Role
admin.site.register(Role)
admin.site.register(Branch)
