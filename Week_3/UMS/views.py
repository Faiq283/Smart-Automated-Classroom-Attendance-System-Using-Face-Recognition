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

        try:
            user = CustomUser.objects.get(username=username)
            if user.status != "approved":
                return render(request, 'login.html', {'error': 'Your account is not approved yet!'})

            if not user.check_password(password):
                return render(request, 'login.html', {'error': 'Invalid Credentials'})

            login(request, user)  # ✅ User ko login karna

            # ✅ Different dashboards ke liye redirect
            if user.user_type == "student":
                return redirect(reverse("student_dashboard"))
            elif user.user_type == "faculty":
                return redirect(reverse("faculty_dashboard"))

        except CustomUser.DoesNotExist:
            pass  # ✅ Agar user nahi mila to authenticate se check karenge

        user = authenticate(request, username=username, password=password)
        if user is not None and isinstance(user, AdminUser):
            login(request, user)
            return redirect(reverse("admin_dashboard"))

        return render(request, 'login.html', {'error': 'Invalid Credentials'})

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

# ✅ Admin Dashboard (Fixed Version)
# ✅ Admin Dashboard
@login_required(login_url='login')
def admin_dashboard(request):
    total_users = CustomUser.objects.count()  # ✅ Total users count
    total_students = CustomUser.objects.filter(user_type='student').count()
    total_faculty = CustomUser.objects.filter(user_type='faculty').count()
    total_departments = Department.objects.count()  # ✅ Total departments count
    total_programs = Program.objects.count()  # ✅ Total programs count

    users = CustomUser.objects.all().order_by('-id')  # ✅ Latest users first
    paginator = Paginator(users, 10)  # ✅ 10 users per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'total_users': total_users,
        'total_students': total_students,
        'total_faculty': total_faculty,
        'total_departments': total_departments,
        'total_programs': total_programs,
        'users': page_obj,  # ✅ Paginated users
    }
    
    return render(request, 'Admin/dashboard.html', context)


# ✅ Logout Function
@login_required
def Logout(request):
    logout(request)
    return redirect('login')  # ✅ Redirect to login page

# SECRET_KEY_REQUIRED = "ums001"  # ✅ Define secret key


# def admin_signup(request, secret_key):
#     if secret_key != SECRET_KEY_REQUIRED:  
#         return HttpResponseForbidden("Access Denied!")  # ✅ Secure access

#     if request.method == "POST":
#         username = request.POST.get("username")
#         email = request.POST.get("email")
#         password = request.POST.get("password")

#         if not username or not password or not email:
#             return render(request, 'Admin/signup.html', {'error': 'All fields are required!'})

#         hashed_password = make_password(password)

#         # ✅ Agar admin pehle se mojood hai, to update kar do
#         admin_user = AdminUser.objects.filter(email=email).first()
#         if admin_user:
#             admin_user.username = username
#             admin_user.password = hashed_password
#             admin_user.save()
#             return render(request, 'login', {'success': 'Admin details updated!'})

#         else:
#             # ✅ Naya admin create karo agar pehle nahi hai
#             new_admin = AdminUser(username=username, email=email, password=hashed_password)
#             new_admin.save()

#         return redirect('login')  # ✅ Redirect to custom login page

#     return render(request, 'Admin/signup.html')  # ✅ Render custom template












