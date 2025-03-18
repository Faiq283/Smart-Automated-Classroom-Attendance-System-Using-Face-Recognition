from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# forms
from ...forms import SemesterForm

# models
from ...models import Semester

# Semester index
@login_required(login_url='login')
def semester_index(request):
    Semesters = Semester.objects.all()
    return render(request, 'Admin/semester/index.html', {'Semesters':Semesters,})

# Semester create
@login_required(login_url='login')
def semester_create(request):
    if request.method == 'POST':
        semester_name = request.POST.get('semester_name')
        form = SemesterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Semester added successfully!')
            return redirect('semester_index')
        else:          
            errors = form.errors.as_data()
            if not  semester_name:
                messages.error(request, 'Semester Name is required.')
            if 'start_date' in errors:
                messages.error(request, 'Start Date is required.')
            if 'end_date' in errors:
                messages.error(request, 'End Date is required.')
            elif Semester.objects.filter(semester_name=semester_name).exists():
                messages.error(request, 'Semester name is already exists.')
    else:
        form = SemesterForm()
    Semesters = Semester.objects.all()
    return render(request, 'Admin/semester/create.html', {'form': form, 'Semesters': Semesters})


# Semester Show
@login_required(login_url='login')
def semester_show(request, pk):
    Semesters = get_object_or_404(Semester, pk=pk)
    return render(request, 'Admin/semester/show.html', {'Semesters': Semesters})

# Semester Edit
@login_required(login_url='login')
def semester_edit(request, pk):
    Semesters = get_object_or_404(Semester, pk=pk)
    if request.method == 'POST':
        form = SemesterForm(request.POST, instance=Semesters)
        if form.is_valid():
            form.save()
            messages.success(request, 'Semester details updated successfully.')               
            return redirect('course_index')
    else:
        form = SemesterForm(instance=Semesters)
    return render(request, 'Admin/semester/edit.html', {'form': form, 'Semesters': Semesters})

# Semester Delete
@login_required(login_url='login')
def semester_delete(request, pk):
    Semesters = get_object_or_404(Semester, pk=pk)
    if request.method == 'POST':
        Semesters.delete()
        messages.success(request, 'Semester Record deleted successfully!')
        return redirect('semester_index')
    return redirect('semester_index')

# Semester status toggle
@login_required(login_url='login')
def semester_toggle(request, id):
    semester = get_object_or_404(Semester, id=id)
    if request.method == 'POST':
        # Toggle the `is_current` field
        semester.is_current = not semester.is_current
        semester.save()

        if semester.is_current:
            messages.success(request, 'Semester has been activated successfully.')
        else:
            messages.success(request, 'Semester has been set to inactive successfully.')

    return redirect('semester_index')