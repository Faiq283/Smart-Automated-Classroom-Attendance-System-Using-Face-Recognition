from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# forms
from ...forms import CourseAssignForm
# models
from ...models import CourseAssign,Faculty,SemCourses


# Course index
@login_required(login_url='login')
def Assigncourse_index(request):
    CoursesAssign = CourseAssign.objects.all()
    faculties = Faculty.objects.all()
    SemCourse = SemCourses.objects.all()
    return render(request, 'Admin/CoursesAssign/index.html', {'CoursesAssign':CoursesAssign,'faculties':faculties,'SemCourse':SemCourse})

# Course create
@login_required(login_url='login')
def Assigncourse_create(request):
    if request.method == 'POST':
        # course_id = request.POST.get('course_id')
        form = CourseAssignForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Assign Course added successfully!')
            return redirect('Assigncourse_index')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)

    else:
        form = CourseAssignForm()
    faculties = Faculty.objects.all()
    SemCourse = SemCourses.objects.all()
    return render(request, 'Admin/CoursesAssign/create.html', {'form': form, 'faculties': faculties, 'SemCourse': SemCourse})


# Course Show
@login_required(login_url='login')
def Assigncourse_show(request, pk):
    CoursesAssign = get_object_or_404(CourseAssign, pk=pk)
    return render(request, 'Admin/CoursesAssign/show.html', {'CoursesAssign': CoursesAssign})

# Course Edit
@login_required(login_url='login')
def Assigncourse_edit(request, pk):
    CoursesAssign = get_object_or_404(CourseAssign, pk=pk)
    if request.method == 'POST':
        form = CourseAssignForm(request.POST, instance=CoursesAssign)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course Assign details updated successfully.')               
            return redirect('Assigncourse_index')
    else:
        form = CourseAssignForm(instance=CoursesAssign)
    return render(request, 'Admin/CoursesAssign/edit.html', {'form': form,})

# Course Delete
@login_required(login_url='login')
def Assigncourse_delete(request, pk):
    CoursesAssign = get_object_or_404(CourseAssign, pk=pk)
    if request.method == 'POST':
        CoursesAssign.delete()
        messages.success(request, 'Course Assign deleted successfully!')
        return redirect('Assigncourse_index')
    return redirect('Assigncourse_index')