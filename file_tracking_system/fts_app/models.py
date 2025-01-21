from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
import uuid

class Branch(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=255, unique=True)
    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True, blank=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)

    groups = models.ManyToManyField(
        Group,
        related_name="customuser_set",
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_set",
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )
    
class File(models.Model):
    file_number = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    subject = models.CharField(max_length=255)
    created_by = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, related_name='created_files')

    def __str__(self):
        return f"File {self.file_number}"


class Tippani(models.Model):
    file = models.ForeignKey(File, on_delete=models.CASCADE, related_name='tippanis')
    subject = models.CharField(max_length=255)

    def __str__(self):
        return f"Tippani for File {self.file.file_number}"


class SupportingDocument(models.Model):
    tippani = models.ForeignKey(Tippani, on_delete=models.CASCADE, related_name='supporting_documents')
    document_name = models.CharField(max_length=255)
    document_path = models.FileField(upload_to='supporting_documents/')

    def __str__(self):
        return self.document_name


class Submission(models.Model):
    STATUS_CHOICES = [
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('transferred', 'Transferred'),
    ]
    tippani = models.ForeignKey(Tippani, on_delete=models.CASCADE, related_name='submissions')
    submitted_by = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='submitted_tippanis')
    submitted_to = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='received_tippanis')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='transferred')
    approval_status = models.BooleanField(default=False)
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Submission of {self.tippani.file.file_number} by {self.submitted_by.name} to {self.submitted_to.name}"
    

