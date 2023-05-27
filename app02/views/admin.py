from django.shortcuts import render, redirect
from app02.models import *
from app02.modelForm.modelForm import *
from Webtest.utils.Pagination import Pagination

# Create your views here.

def admin_list(request):

    data_dict = {}
    search_data = request.GET.get('q', '')
    if search_data:
        data_dict['username__contains'] = search_data

    data_list = Admin.objects.filter(**data_dict)
    page_object = Pagination(request, data_all_list=data_list)

    context = {
        'data_list': page_object.data_list,

        'search_data': search_data,
        'page_string': page_object.html(),
    }

    return render(request, 'admin_list.html', context)

def admin_add(request):


    if request.method == 'GET':
        formset = Admin_form()
        return render(request, 'A.html', {'formset': formset, 'title': '新建管理员'})

    formset = Admin_form(data=request.POST)
    if formset.is_valid():
        formset.save()
        return redirect('/app02/admin/list/')
    else:
        return render(request, 'A.html', {'formset': formset, 'title': '新建管理员'})

def admin_edit(request, nid):
    obj = Admin.objects.filter(id=nid).first()
    if obj is None:
        return render(request, '404.html', {'msg': '用户不存在喵'})
    if request.method == 'GET':
        formset = Admin_form(instance=obj)
        return render(request, 'A.html', {'formset': formset, 'title': '编辑管理员'})

    formset = Admin_form(data=request.POST, instance=obj)
    if formset.is_valid():
        formset.save()
        return redirect('/app02/admin/list/')
    else:
        return render(request, 'A.html', {'formset': formset, 'title': '编辑管理员'})

def admin_delete(request, nid):
    Admin.objects.filter(id=nid).delete()
    return redirect('/app02/admin/list/')