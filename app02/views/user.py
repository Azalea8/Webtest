from django.shortcuts import render, redirect
from app02.models import *
from app02.modelForm.modelForm import *
from Webtest.utils.Pagination import Pagination

# Create your views here.

def user_list(request):

    data_list = InfoUser.objects.all()
    # for obj in data_list:
    #     obj.create_time = obj.create_time.strftime('%Y-%m-%d')
    #     obj.gender = obj.get_gender_display()
    page_object = Pagination(request, data_all_list=data_list,)
    context = {
        'data_list': page_object.data_list,
        'page_string': page_object.html(),
    }
    return render(request, 'user_list.html', context)

def user_add(request):
    if request.method == 'GET':
        context = {
            'gender_choices':InfoUser.gender_choices,
            'depart_list':Department.objects.all()
        }
        return render(request, 'user_add.html',context)

    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    age = request.POST.get('age')
    account = request.POST.get('account')
    time = request.POST.get('time')
    depart_id = request.POST.get('depart')
    gender = request.POST.get('gender')

    InfoUser.objects.create(name=name, password=pwd, age=age,
                            account=account, create_time=time,
                            depart_id=depart_id, gender=gender)

    return redirect('/app02/user/list/')

def user_model_add(request):
    if request.method == "GET":
        formset = User_model_form()
        return render(request, 'A.html', {'formset': formset, 'title': '新建用户'})

    formset = User_model_form(data=request.POST)
    if formset.is_valid():
        formset.save()
        return redirect('/app02/user/list/')
    else:
        return render(request, 'A.html', {'formset': formset, 'title': '新建用户'})

def user_edit(request, nid):
    obj = InfoUser.objects.filter(id=nid).first()

    if request.method == "GET":
        formset = User_model_form(instance=obj)
        return render(request, 'A.html', {'formset': formset, 'title': '编辑用户'})

    formset = User_model_form(data=request.POST, instance=obj)
    if formset.is_valid():
        # 表单中没有的，写死到数据库
        # formset.instance.password = ...
        formset.save()
        return redirect('/app02/user/list/')
    else:
        return render(request, 'A.html', {'formset': formset, 'title': '编辑用户'})

def user_delete(request, nid):
    InfoUser.objects.filter(id=nid).delete()
    return redirect('/app02/user/list/')