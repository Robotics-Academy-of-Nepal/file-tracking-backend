from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    Loan, Office, Awards, Punishments, Education, Department, CustomUser,
    Designation, Tippani, LettersAndDocuments, File, Approval
)

# Customize the UserAdmin for CustomUser
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'employee_id', 'employee_type', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email', 'employee_id')
    list_filter = ('employee_type', 'is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('email', 'employee_id', 'employee_type')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'employee_id', 'employee_type', 'password1', 'password2'),
        }),
    )

# Register the CustomUser model with the custom admin class
admin.site.register(CustomUser, CustomUserAdmin)

# Register other models
@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ('name', 'loan_type', 'interest_rate', 'max_amount', 'min_amount', 'max_tenure', 'min_tenure')
    search_fields = ('name', 'loan_type')
    list_filter = ('loan_type',)

@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    list_display = ('office_name', 'position', 'position_category', 'duration')
    search_fields = ('office_name', 'position')
    list_filter = ('position_category',)

@admin.register(Awards)
class AwardsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(Punishments)
class PunishmentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('institution', 'education_level', 'board', 'percentage', 'year')
    search_fields = ('institution', 'education_level', 'board')
    list_filter = ('education_level',)

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(Designation)
class DesignationAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Tippani)
class TippaniAdmin(admin.ModelAdmin):
    list_display = ('present_subject', 'present_by', 'present_date', 'approved_by', 'approve_date')
    search_fields = ('present_subject', 'present_by')
    list_filter = ('present_date', 'approve_date')

@admin.register(LettersAndDocuments)
class LettersAndDocumentsAdmin(admin.ModelAdmin):
    list_display = ('registration_no', 'invoice_no', 'date', 'subject', 'letter_date', 'sending_office', 'receiving_office')
    search_fields = ('registration_no', 'invoice_no', 'subject')
    list_filter = ('date', 'letter_date')

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('letter_document', 'file')
    search_fields = ('letter_document__subject',)

@admin.register(Approval)
class ApprovalAdmin(admin.ModelAdmin):
    list_display = ('tippani', 'submitted_by', 'approved_by', 'status', 'approved_date')
    search_fields = ('tippani__present_subject', 'submitted_by__name', 'approved_by__name')
    list_filter = ('status', 'approved_date')