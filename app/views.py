from django.shortcuts import render, redirect
from .models import *
from django.shortcuts import get_object_or_404

def index(request):
    return render(request, "index.html")

def create(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')
        phone = request.POST.get('phone_number')
        email = request.POST.get('email')

        Students.objects.create(
            first_name = first_name,
            last_name = last_name,
            address = address,
            phone = phone,
            email = email,
            date_registered = datetime.now()
        )
        return redirect('read')
    return render(request, "create.html")


def update(request):
    students = Students.objects.all()

    context = {
        'students':students
    }
    return render(request, "update.html", context)

def update_form(request, student_id):
    student = get_object_or_404(Students, pk=student_id)

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')
        phone = request.POST.get('phone_number')
        email = request.POST.get('email')
        
        student.first_name = first_name
        student.last_name = last_name
        student.address = address
        student.phone = phone
        student.email = email

        student.save()
        return redirect('Update')
    
    context = {
        'student': student
    }
    return render(request, "update_form.html", context)

def read(request):
    students = Students.objects.all()

    context = {
        'students':students
    }
    return render(request, "read.html", context)

def del_render(request):
    students = Students.objects.all()

    context = {
        'students':students
    }
    return render(request, "delete.html", context)


def delete(request, student_id):
    student = get_object_or_404(Students, pk=student_id)
    if request.method == "POST":
        student.delete()
        return redirect('deleted')
    return render(request, "read.html", {'student': student})



