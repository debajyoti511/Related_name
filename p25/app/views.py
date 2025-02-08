from django.shortcuts import render
from .forms import *
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'home.html')


def insert_school(request):
    ESFO = SchoolForm()
    d = {'ESFO': ESFO}
    if request.method == 'POST':
        SDFO = SchoolForm(request.POST)
        if SDFO.is_valid():
            SDFO.save()
            return HttpResponse('Done....')
    return render(request, 'insert_school.html', d)

def insert_student(request):
    ESFO = StudentForm()
    d = {'ESFO': ESFO}
    if request.method == 'POST':
        SDFO = StudentForm(request.POST)
        if SDFO.is_valid():
            SDFO.save()

    return render(request, 'insert_student.html', d)


def lists(request):
    allschools = School.objects.all()
    d = {'schools': allschools}
    return render(request, 'lists.html', d)


def display(request, pk):
    SO = School.objects.get(pk=pk)
    d = {'SO': SO}
    return render(request, 'display.html', d)