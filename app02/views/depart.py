from django.shortcuts import render, redirect
from app02.models import *
from app02.modelForm.modelForm import *
from Webtest.utils.Pagination import Pagination

# Create your views here.


def depart_list(request):

    data_list = Department.objects.all()
    page_object = Pagination(request, data_all_list=data_list)
    context = {
        'data_list': page_object.data_list,
        'page_string': page_object.html(),
    }
    return render(request, 'depart_list.html', context)

def depart_add(request):
    if request.method == 'GET':
        return render(request, 'depart_add.html')

    title = request.POST.get('title')
    Department.objects.create(title=title)

    return redirect('/app02/depart/list/')

def depart_delete(request):

    nid = request.GET.get('nid')
    Department.objects.filter(id=nid).delete()

    return redirect('/app02/depart/list/')

def depart_edit(request, nid):
    if request.method == 'GET':
        obj = Department.objects.filter(id=nid).first()
        return render(request, 'depart_edit.html', {'obj':obj})

    title = request.POST.get('title')
    Department.objects.filter(id=nid).update(title=title)

    return redirect('/app02/depart/list/')