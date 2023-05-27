from django.shortcuts import render, redirect, HttpResponse
from app02.models import *
from app02.modelForm.modelForm import *
from Webtest.utils.Pagination import Pagination
from django import forms

# Create your views here.

class LoginForm(forms.Form):
    username = forms.CharField(
        label='用户名',
        widget=forms.TextInput(attrs={'placeholder': '这里填写用户名喵', 'class': 'form-control'})
    )
    password = forms.CharField(
        label='密码',
        widget=forms.PasswordInput(attrs={'placeholder': '这里输入密码喵', 'class': 'form-control'})

    )

    def clean_password(self):
        pwd = self.cleaned_data.get('password')
        return md5(pwd)

def login(request):
    if request.method == 'GET':
        formset = LoginForm()
        return render(request, 'login.html', {'formset': formset})

    formset = LoginForm(data=request.POST)
    if formset.is_valid():
        # print(formset.cleaned_data)
        admin_object = Admin.objects.filter(**formset.cleaned_data).first()
        if admin_object:
            request.session['info'] = {'id': admin_object.id, 'username': admin_object.username}
            return redirect('/app02/admin/list/')
        else:
            # 向form组件主动添加错误信息
            formset.add_error('password', '用户名或密码错误了喵，再试试看~')
            return render(request, 'login.html', {'formset': formset})
    else:
        return render(request, 'login.html', {'formset': formset})

def logout(request):
    request.session.clear()
    return redirect('/app02/login/')