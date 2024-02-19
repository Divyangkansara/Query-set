from django.shortcuts import render
from .models import Student, Teacher
from django.db.models import Avg, Max, Min, Sum, Count
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
    #student_data = Student.objects.filter(city__startswith = 'b') | Student.objects.filter(city__startswith = 'a')
    # student_data = Student.objects.filter(id__range = (1,6))
    # student_data = Student.objects.create(name='Divyang', roll=101, city='Ahmedabad', marks=89)
    # student_data.save()

    #student_data = Student.objects.bulk_create([Student(name='Chintan',roll=102,city='Baroda',marks=70),Student(name='Shubham',roll=103,city='Patan',marks=60)])
    # student_data = Student.objects.filter(roll=101,name='Divyang')
    # student_data = Student.objects.all()[0:11]      #[:11:2]
    # student_data = Student.objects.all()[0]   #for single element
    # student_data = Student.objects.all().order_by('marks')    #ASC
    # student_data = Student.objects.all().order_by('-marks')   #DESC
    # student_data = Student.objects.all().order_by('roll', '-marks')


    ##################### Aggregate Functions #############


    # student_data = Student.objects.all().aggregate(Avg('marks'))
    # student_data = Student.objects.all().aggregate(Min('marks'))
    # student_data = Student.objects.all().aggregate(Max('marks'))
    # student_data = Student.objects.all().aggregate(Sum('marks'))
    student_data = Student.objects.all().aggregate(Count('name'))
    data = Student.objects.all().count()
    # deletedata = Student.objects.all().delete()

    print("Return:", student_data)
    print(data)
    # print("SQL Query:", student_data.query)

    return render(request, 'lookups/home.html', {'student_data': student_data})


def teacher_fun(request):
    teacher_data = Teacher.objects.all()
    print("Return:", teacher_data)
    print()
    print("SQL Query:", teacher_data.query)

    return render(request, 'lookups/teacher.html', {'teacher_data': teacher_data})



