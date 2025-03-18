from django.urls import path
from .views import home, login_view, admin_dashboard,Logout ,student_dashboard,faculty_dashboard, password_reset
from .controller.admin import users_views, university_views, campus_views


urlpatterns = [
    path('', home, name='home'),  # Home Page
    path('login/', login_view, name='login'),  # Login Page (Sab k liye)
    path('password_reset/', password_reset, name='password_reset'),
    # path('custom-admin/signup/<str:secret_key>/', admin_signup, name='admin_signup'),  # ✅ Dynamic Secret Key
    path('admin/dashboard/', admin_dashboard, name='admin_dashboard'),  # Admin Dashboard
    path('logout/', Logout, name='logout'),  # ✅ Logout URL

    # Users Views
    path('admin/register/', users_views.register_user, name='register_user'),
    path('admin/approve/<int:user_id>/', users_views.approve_user, name='approve_user'),
    path('delete-user/<int:user_id>/', users_views.delete_user, name='delete_user'),

   # University URLs
    path('university/', university_views.university_index, name='university_index'),
    path('university/create/', university_views.university_create, name='university_create'),
    path('university/<int:pk>/', university_views.university_show, name='university_show'),
    path('university/<int:pk>/edit/', university_views.university_edit, name='university_edit'),
    path('university/<int:pk>/delete/', university_views.university_delete, name='university_delete'),

    # Campus URLs
    path('campus/', campus_views.campus_index, name='campus_index'),
    path('campus/create/', campus_views.campus_create, name='campus_create'),
    path('campus/<int:pk>/', campus_views.campus_show, name='campus_show'),
    path('campus/<int:pk>/edit/', campus_views.campus_edit, name='campus_edit'),
    path('campus/<int:pk>/delete/', campus_views.campus_delete, name='campus_delete'),

    # path('token=<str:secret_key>/', admin_signup, name='admin_signup'),
    #user urls
    path('users/', users_views.user_index, name='user_index'),
    # path('users/create/', users_views.user_create, name='user_create'),
    # path('users/update/<int:pk>/', users_views.user_update, name='user_update'),
    # path('users/delete/<int:pk>/', users_views.user_delete, name='user_delete'),
    # path('toggle_user_status/', users_views.toggle_user_status, name='user_block_toggle'),

    path('student/dashboard/', student_dashboard, name='student_dashboard'),
    path('faculty/dashboard/', faculty_dashboard, name='faculty_dashboard'),
]



