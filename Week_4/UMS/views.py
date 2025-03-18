from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import PasswordResetForm
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.db.models import Count, Q
from django.core.paginator import Paginator
from django.urls import reverse
from django.contrib import messages
from django.utils.crypto import get_random_string

from .models import AdminUser, CustomUser, Department, Program
from .forms import RegisterUserForm
from .utils import send_approval_email

# ✅ Home Page
def home(request):
    return render(request, 'home.html')

# ✅ Login View
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = None
        try:
            user = CustomUser.objects.get(username=username)
            if user.status != "approved":
                messages.error(request, "Your account is not approved yet!")
                return redirect('login')

            if not user.check_password(password):
                messages.error(request, "Invalid Credentials")
                return redirect('login')

            login(request, user)

            # ✅ Redirect based on user type
            return redirect(reverse(f"{user.user_type}_dashboard"))

        except CustomUser.DoesNotExist:
            user = authenticate(request, username=username, password=password)

        if user and isinstance(user, AdminUser):
            login(request, user)
            return redirect(reverse("admin_dashboard"))

        messages.error(request, "Invalid Credentials")
        return redirect('login')

    return render(request, 'login.html')

# ✅ Password Reset View
def password_reset(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save(request=request)
            messages.success(request, "Check your email for password reset instructions.")
            return redirect('login')  # ✅ Redirect to login page
    else:
        form = PasswordResetForm()

    return render(request, 'resetpassword.html', {'form': form})

# ✅ Student Dashboard
@login_required
def student_dashboard(request):
    messages.success(request, "You are Successfully logged in as Student")
    return render(request, "student/dashboard.html")

# ✅ Faculty Dashboard
@login_required
def faculty_dashboard(request):
    messages.success(request, "You are Successfully logged in as Faculty")
    return render(request, "faculty/dashboard.html")

# ✅ Admin Dashboard
@login_required(login_url='login')
def admin_dashboard(request):
    total_users = CustomUser.objects.count()
    total_students = CustomUser.objects.filter(user_type='student').count()
    total_faculty = CustomUser.objects.filter(user_type='faculty').count()
    total_departments = Department.objects.count()
    total_programs = Program.objects.count()
    total_courses = Program.objects.count()  # Assuming this represents courses
    total_semester = 8  # ✅ Define the total semesters (adjust as needed)

    users = CustomUser.objects.all().order_by('-id')
    paginator = Paginator(users, 10)  # ✅ 10 users per page
    page_number = request.GET.get('page')

    try:
        page_obj = paginator.page(page_number) if page_number else paginator.page(1)
    except:
        page_obj = paginator.page(1)

    context = {
        'total_users': total_users,
        'total_students': total_students,
        'total_faculty': total_faculty,
        'total_departments': total_departments,
        'total_programs': total_programs,
        'total_semester': total_semester,
        'total_courses': total_courses,
        'users': page_obj,  # ✅ Paginated users
    }
    
    return render(request, 'Admin/dashboard.html', context)

# ✅ Logout Function
@login_required
def Logout(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('login')  # ✅ Redirect to login page
