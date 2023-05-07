from django.shortcuts import render

from .models import Employee


def show_employees(request):
    employees = Employee.objects.all()
    return render(request, 'employees_list.html', {'employees': employees})