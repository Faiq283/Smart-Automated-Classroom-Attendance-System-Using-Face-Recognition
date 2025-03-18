from django.contrib.auth.models import AbstractUser
from django.db import models

class AdminUser(AbstractUser):
    is_admin = models.BooleanField(default=True)

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="admin_users",
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="admin_users_permissions",
        blank=True
    )

    def __str__(self):
        return self.username


class CustomUser(AbstractUser):
    USER_TYPES = (
        ('faculty', 'Faculty'),
        ('student', 'Student'),
    )
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPES, default='student')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    unique_id = models.CharField(max_length=20, unique=True, blank=True)  # ✅ Unique ID auto-generate hoga

    def __str__(self):
        return self.username

# university model
class University(models.Model):
    id = models.AutoField(primary_key=True)
    uni_id = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    # created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['id']
    


# campus model
class Campus(models.Model):
    id = models.AutoField(primary_key=True)
    campus_id = models.CharField(max_length=255, unique=True, default='TEMP_ID')  
    university = models.ForeignKey(University, to_field='uni_id', on_delete=models.CASCADE, related_name='campuses')
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)  # ✅ Add this line
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']


# department model
class Department(models.Model):
    id = models.AutoField(primary_key=True)
    department_id = models.CharField(max_length=255, unique=True)
    campus = models.ForeignKey(Campus,to_field='campus_id', on_delete=models.CASCADE, related_name='departments')
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['id']


# program model
class Program(models.Model):
    id = models.AutoField(primary_key=True)
    program_id = models.CharField(max_length=255, unique=True)
    department = models.ForeignKey(Department,to_field='department_id', on_delete=models.CASCADE, related_name='programs')
    name = models.CharField(max_length=255)
    duration_year = models.PositiveIntegerField()
    total_credits = models.PositiveIntegerField()
    degree_type = models.CharField(max_length=255)
    program_description = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Meta:
    ordering = ['id']

