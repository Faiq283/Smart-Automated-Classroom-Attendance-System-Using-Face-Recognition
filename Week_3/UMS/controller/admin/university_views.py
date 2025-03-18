from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# forms
from ...forms import UniversityForm
# models
from ...models import University


# university views
@login_required(login_url='login')
def university_index(request):
    universities = University.objects.all()
    page_title = "University | List"
    return render(request, 'Admin/university/index.html', {'universities': universities, 'page_title': page_title})

@login_required(login_url='login')
def university_create(request):
    if request.method == "POST":
        uni_id = request.POST.get('uni_id')
        form = UniversityForm(request.POST)

        # Check if the University ID already exists
        if uni_id and University.objects.filter(uni_id=uni_id).exists():
            messages.error(request, 'This University Code already exists.')
        elif form.is_valid():
            form.save()
            messages.success(request, 'University added successfully!')
            return redirect('university_index')
        else:
            # Handle form validation errors
            errors = form.errors.as_data()
            if not uni_id:
                messages.error(request, 'University Code field is required.')
            if 'name' in errors:
                messages.error(request, 'University Name field is required.')
            if 'location' in errors:
                messages.error(request, 'Location field is required.')
    else:
        form = UniversityForm()
    
    page_title = "University | Add"
    return render(request, 'Admin/university/create.html', {'form': form, 'page_title': page_title})


@login_required(login_url='login')
def university_show(request, pk):
    university = get_object_or_404(University, pk=pk)
    page_title = "University | Show"
    return render(request, 'Admin/university/show.html', {'university': university,'page_title': page_title})

# university edit logic
@login_required(login_url='login')
def university_edit(request, pk):
    university = get_object_or_404(University, pk=pk)
    
    if request.method == 'POST':
        name = request.POST.get('name')
        location = request.POST.get('location')
        
        # Validation
        if not name:
            messages.error(request, 'University name is required.')
        if not location:
            messages.error(request, 'Location is required.')
        
        if name and location:
            university.name = name
            university.location = location
            university.save()
            
            messages.success(request, 'University details updated successfully.')
            return redirect('university_index')
    page_title = "University | Edit"
    return render(request, 'Admin/university/edit.html',{'university': university,'page_title': page_title})

@login_required(login_url='login')
def university_delete(request, pk):
    university = get_object_or_404(University, pk=pk)
    if request.method == 'POST':
        university.delete()
        messages.success(request, 'University deleted successfully!')
        return redirect('university_index')
    return redirect('university_index')