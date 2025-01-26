from django.contrib import admin
from .models import CustomUser , Loan, Education, Awards, Punishments, Office 

# Register the CustomUser model

admin.site.register(CustomUser)
admin.site.register(Loan)
admin.site.register(Education)
admin.site.register(Awards)
admin.site.register(Punishments)
admin.site.register(Office)
