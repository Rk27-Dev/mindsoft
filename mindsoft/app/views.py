from django.shortcuts import render
from app.forms import *
from app.models import *
from django.http import HttpResponse
# Create your views here.
def auth_view(request):
    # form=auth_form()
    if request.method=='POST':
        form=auth_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('saved data')
    else:
        form=auth_form()
        return  render(request,'auth.html',{'form':form})


def dept_view(request):
    # form=auth_form()
    if request.method=='POST':
        form=dept_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('saved data')
    else:
        form=dept_form()
        return  render(request,'dept.html',{'form':form})