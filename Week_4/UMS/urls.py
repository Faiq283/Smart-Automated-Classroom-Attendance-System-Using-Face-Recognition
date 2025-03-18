from django.urls import path
from .views import home, login_view, admin_dashboard,Logout ,student_dashboard,faculty_dashboard, password_reset
from .controller.admin import users_views, university_views, campus_views, department_views, program_views, course_views, semester_views, semCourse_views


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

     # department urls
    path('department/', department_views.department_index, name='department_index'),
    path('department/create/', department_views.department_create, name='department_create'),
    path('department/<int:pk>/', department_views.department_show, name='department_show'),
    path('department/<int:pk>/edit/', department_views.department_edit, name='department_edit'),
    path('department/<int:pk>/delete/', department_views.department_delete, name='department_delete'),

    # program urls
    path('programs/', program_views.programs_index, name='programs_index'),
    path('programs/create/', program_views.program_create, name='program_create'),
    path('programs/<int:pk>/', program_views.programs_show, name='programs_show'),
    path('programs/<int:pk>/edit/', program_views.programs_edit, name='programs_edit'),
    path('programs/<int:pk>/delete/', program_views.programs_delete, name='programs_delete'),

    # courses urls
    path('course/', course_views.course_index, name='course_index'),
    path('course/create/', course_views.course_create, name='course_create'),
    path('course/<int:pk>/', course_views.course_show, name='course_show'),
    path('course/<int:pk>/edit/', course_views.course_edit, name='course_edit'),
    path('course/<int:pk>/delete/', course_views.course_delete, name='course_delete'),

    # semester urls
    path('semester/', semester_views.semester_index, name='semester_index'),
    path('semester/create/', semester_views.semester_create, name='semester_create'),
    path('semester/<int:pk>/', semester_views.semester_show, name='semester_show'),
    path('semester/<int:pk>/edit/', semester_views.semester_edit, name='semester_edit'),
    path('semester/<int:pk>/delete/', semester_views.semester_delete, name='semester_delete'),
    path('semester/<int:id>/toggle/', semester_views.semester_toggle, name='semester_toggle'),
    
    # semester course urls
    path('semesterCourse/', semCourse_views.semesterCourse_index, name='semesterCourse_index'),
    path('semesterCourse/create/', semCourse_views.semesterCourse_create, name='semesterCourse_create'),
    path('semesterCourse/<int:pk>/', semCourse_views.semesterCourse_show, name='semesterCourse_show'),
    path('semesterCourse/<int:pk>/edit/', semCourse_views.semesterCourse_edit, name='semesterCourse_edit'),
    path('semesterCourse/<int:pk>/delete/', semCourse_views.semesterCourse_delete, name='semesterCourse_delete'),  

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



