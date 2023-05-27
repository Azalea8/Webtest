from django.shortcuts import render, redirect, HttpResponse
from app02.models import *
from app02.modelForm.modelForm import *
from Webtest.utils.Pagination import Pagination
from django import forms

# Create your views here.

def task_list(request):

    return render(request, 'task_list.html')