from django.contrib import admin
from .models import Student, Teacher
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'roll', 'city','marks')
    # list_filter =     ('roll', 'city', 'passdate', 'datetime')
    # search_fields = ('name', 'roll', 'city','marks', 'passdate', 'datetime')

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'department')
    # list_filter =     ('roll', 'city', 'passdate', 'datetime')
    # search_fields = ('name', 'roll', 'city','marks', 'passdate', 'datetime')