from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

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

# course model
class Course(models.Model):
    id = models.AutoField(primary_key=True)
    course_id = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    course_description = models.TextField()
    program = models.ForeignKey(Program,to_field='program_id', on_delete=models.CASCADE, related_name='courses')
    credits = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']


        
# semster model
class Semester(models.Model):
    id = models.AutoField(primary_key=True)    
    semester_name = models.CharField(max_length=100, unique=True)
    start_date = models.DateField()
    end_date = models.DateField()
    is_current = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.semester_name  # Display the semester name
        
# semster course model
class SemCourses(models.Model):
    id = models.AutoField(primary_key=True)
    sem_course_id = models.CharField(max_length=255, unique=True)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    course = models.ForeignKey(Course,to_field='course_id', on_delete=models.CASCADE)
    max_students = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']

def save(self, *args, **kwargs):
        # Print or log the course name for debugging purposes
        if self.course:
            print(self.course.name)  # Access the course name correctly
        super().save(*args, **kwargs)  # Call the original save method        
        



