from django.shortcuts import render, redirect
from app02.models import *
from app02.modelForm.modelForm import *
from Webtest.utils.Pagination import Pagination

# Create your views here.

def pretty_list(request):

    data_dict = {}
    search_data = request.GET.get('q', '')
    if search_data:
        data_dict['mobile__contains'] = search_data

    data_all_list = PrettyNum.objects.filter(**data_dict).order_by('-level')
    page_object = Pagination(request, data_all_list=data_all_list)

    context = {'data_list': page_object.data_list, 'search_data': search_data,
               # 实现分页的参数
               'page_string': page_object.html()
               }

    return render(request, 'pretty_list.html', context)

def pretty_add(request):
    if request.method == 'GET':
        formset = Pretty_num_form()
        return render(request, 'A.html', {'formset':formset, 'title': '新建靓号'})

    formset = Pretty_num_form(data=request.POST)
    if formset.is_valid():
        formset.save()
        return redirect('/app02/prettynum/list/')
    else:
        return render(request, 'A.html', {'formset': formset, 'title': '新建靓号'})

def pretty_delete(request, nid):
    PrettyNum.objects.filter(id=nid).delete()
    return redirect('/app02/prettynum/list/')

def pretty_edit(request, nid):
    obj = PrettyNum.objects.filter(id=nid).first()

    if request.method == 'GET':
        formset = Pretty_num_form(instance=obj)
        return render(request, 'A.html', {'formset': formset, 'title': '编辑靓号'})

    formset = Pretty_num_form(data=request.POST, instance=obj)
    if formset.is_valid():
        formset.save()
        return redirect('/app02/prettynum/list/')
    else:
        return render(request, 'A.html', {'formset': formset, 'title': '编辑靓号'})