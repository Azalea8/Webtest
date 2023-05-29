from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from app02.models import *
from app02.modelForm.modelForm import *
from Webtest.utils.Pagination import Pagination
from django import forms

# Create your views here.

def task_list(request):
    data_list = Task.objects.all().order_by('-id')
    formset = TaskModelForm()
    context = {
        'data_list': data_list,
        'formset': formset
    }
    return render(request, 'task_list.html', context)

@csrf_exempt # 免除csrf_tokens检测
def task_ajax(request):

    formset = TaskModelForm(data=request.POST)
    if formset.is_valid():
        formset.save()
        data_dict = {'status': True, }
        return HttpResponse(json.dumps(data_dict))
    else:
        data_dict = {'status': False, 'errors': formset.errors}
        return HttpResponse(json.dumps(data_dict))
