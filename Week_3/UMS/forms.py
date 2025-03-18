from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from .models import CustomUser, University, Campus, Department, Program
import random
import string
from .utils import send_approval_email

class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'user_type', 'status']

    def save(self, commit=True):
        user = super().save(commit=False)
        
        # ✅ Auto Generate Username (firstname + 13550 + increment)
        last_user = CustomUser.objects.filter(username__startswith=user.first_name).order_by('-id').first()
        if last_user:
            last_number = int(last_user.username.replace(user.first_name, ''))
            new_number = last_number + 1
        else:
            new_number = 13550

        user.username = f"{user.first_name}{new_number}"

        # ✅ Generate Random Password
        raw_password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        user.raw_password = raw_password  # ✅ Save for email only
        user.password = make_password(raw_password)

        if commit:
            user.save()
            if user.status == 'Approved':  # ✅ Email Only if Approved
                send_approval_email(user)
        
        return user


# university form
class UniversityForm(forms.ModelForm):
    class Meta:
        model = University
        fields = ['uni_id','name', 'location']


# campus form
class CampusForm(forms.ModelForm):
    class Meta:
        model = Campus
        fields = ['campus_id', 'name', 'location', 'university']


# department form
class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['department_id', 'name', 'description', 'campus']


# program form
class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = '__all__'


