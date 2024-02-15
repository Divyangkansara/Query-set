from django.shortcuts import render
from .models import Student
# Create your views here.

def home(request):
    #student_data = Student.objects.all()
    # # student_data = Student.objects.filter(name__iexact='Rahul')
    # student_data = Student.objects.filter(name__icontains='k')
    # student_data = Student.objects.filter(id__in = [1,5,7])
    #student_data = Student.objects.filter(marks__in = [80])
    # student_data = Student.objects.filter(marks__gt = 70)    #lt
    # student_data = Student.objects.filter(marks__gte = 70)   #lte
    # student_data = Student.objects.filter(name__startswith = 'R')
    student_data = Student.objects.filter(city__startswith = 'b') | Student.objects.filter(city__startswith = 'a')
    # student_data = Student.objects.filter(id__range = (1,6))
    

         
    print("Return:", student_data)
    print()
    print("SQL Query:", student_data.query)
    return render(request, 'lookups/home.html', {'student_data': student_data})
