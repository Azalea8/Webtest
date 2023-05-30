from django.shortcuts import render, redirect, HttpResponse
from app02.models import *
from app02.modelForm.modelForm import *
from Webtest.utils.Pagination import Pagination
from django import forms
from django.views.decorators.csrf import csrf_exempt
import json

import random
from datetime import datetime

def order_list(request):
    formset = OrderModelForm()
    data_list = Order.objects.all().order_by('-id')
    context = {
        'formset': formset,
        'data_list': data_list,
    }
    return render(request, 'order_list.html', context)

@csrf_exempt
def order_add(request):
    formset = OrderModelForm(data=request.POST)
    if formset.is_valid():
        # 后端生成数据插入表单
        formset.instance.oid = datetime.now().strftime('%Y-%m-%d_%H:%M:%S_') + str(random.randint(1000, 10000))
        formset.instance.admin_id = request.session['info'].get('id')

        formset.save()
        data_dict = {'status': True, }
        return HttpResponse(json.dumps(data_dict))
    else:
        data_dict = {'status': False, 'errors': formset.errors}
        return HttpResponse(json.dumps(data_dict))

def order_delete(request):
    nid = request.GET.get('nid')
    print(nid)
    Order.objects.filter(id=nid).delete()
    data_dict = {'status': True, }
    return HttpResponse(json.dumps(data_dict))