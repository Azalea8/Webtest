from django.shortcuts import render, HttpResponse, redirect
from app01.models import *
# Create your views here.

def test(request):
    return render(request, 'test.html')

def test1(request):
    name = '世界充满谎言'
    list = ['百度', '腾讯', '阿里']
    return render(request, 'test1.html', {'name': name, 'list': list})

def news(request):

    import requests
    # 调用api接口 https: // open.tophub.today / hot

    res = requests.get('https://open.tophub.today/hot')
    ans = res.json()
    ans = ans.get('data').get('items')[:20]

    return render(request, 'news.html', {'list': ans})

def something(request):

    print(request.method)

    print(request.GET)

    #return HttpResponse('返回内容')

    return redirect('https://azalea.ink')

def login(request):

    if request.method == 'GET':
        return render(request, 'login.html')

    # print(request.POST)
    username = request.POST.get('user')
    password = request.POST.get('pwd')
    if username == 'root' and password == '123':
        # return HttpResponse('登录成功')
        return redirect('https://azalea.ink')
    else:
        return render(request, 'login.html', {'error_msg': '输入有错误喵~'})

def orm(request):

    # ---------------新建
    # Department.objects.create(title='销售部')
    # Department.objects.create(title='运营部')
    # Department.objects.create(title='IT部')
    # UserInfo.objects.create(name='Azalea', password='lw712722407302', age=19)
    # UserInfo.objects.create(name='1', password='1')

    # ---------------删除
    # UserInfo.objects.filter(name='1').delete()
    # Department.objects.all().delete()

    # ---------------查找
    # data_list [对象，对象，对象...] QuerySet类型
    # data_list = UserInfo.objects.all()
    # for obj in data_list:
    #     print(obj.id, obj.name, obj.password, obj.age)

    # data_list [对象,] 一个元组也是类似列表返回
    # row = UserInfo.objects.filter(id=1).first()
    # print(row.id, row.name, row.password, row.age)

    # ----------------更新
    # UserInfo.objects.filter(name='1').update(password='999')

    return HttpResponse('成功！')

def info_list(request):
    data_list = UserInfo.objects.all()

    return render(request, 'info_list.html', {'data_list': data_list})

def info_add(request):
    if request.method == 'GET':
        return render(request, 'info_add.html')

    user = request.POST.get('user')
    password = request.POST.get('pwd')
    age = request.POST.get('age')

    UserInfo.objects.create(name=user, password=password, age=age)

    return redirect('/app01/info_list/')

def info_delete(request):

    nid = request.GET.get('nid')
    UserInfo.objects.filter(id=nid).delete()

    # return HttpResponse('删除成功！')
    return redirect('/app01/info_list/')