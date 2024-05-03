from django.shortcuts import render
from personal.models import Project

def home(request):
    data = Project.objects.all()
    return render(request,"personal/index.html",{'data':data})
