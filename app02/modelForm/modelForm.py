from django import forms
from app02.models import *
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from Webtest.utils.encrypt import md5

class Bootstrap_model_form(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if 'class' not in field.widget.attrs.keys():
                field.widget.attrs['class'] = 'form-control'
            if 'placeholder' not in field.widget.attrs.keys():
                field.widget.attrs['placeholder'] = field.label


class User_model_form(Bootstrap_model_form):
    class Meta:
        model = InfoUser
        fields = ["name", "password", "age", "account", "create_time", "gender", "depart"]
        widgets = {
           'password': forms.PasswordInput(attrs={'placeholder': '这里填写密码喵~'}, render_value=True),
        }


class Pretty_num_form(Bootstrap_model_form):

    # 后端验证 1
    mobile = forms.CharField(
        label='手机号',
        validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号格式错误喵~')],
        widget=forms.TextInput(attrs={'placeholder': '彩蛋喵~'})
    )

    class Meta:
        model = PrettyNum
        # fields = ['mobile', 'price', 'level', 'status']
        fields = '__all__'
        widgets = {
            # 'mobile': forms.TextInput(attrs={'placeholder': '彩蛋喵~'})
        }

    # 后端验证 2
    def clean_mobile(self):
        txt_mobile = self.cleaned_data['mobile']
        exists = PrettyNum.objects.filter(mobile=txt_mobile).exists()
        if exists:
            raise ValidationError('手机号已存在喵~')
        return txt_mobile

class Admin_form(Bootstrap_model_form):

    confirm_password = forms.CharField(
        label='确认密码',
        widget=forms.PasswordInput(attrs={'placeholder': '再次输入密码喵~'}),

    )

    class Meta:
        model = Admin
        fields = ['username', 'password', 'confirm_password']
        widgets = {
            'password': forms.PasswordInput(attrs={'placeholder': '输入密码喵'}, render_value=True),
        }

    def clean_password(self):
        pwd = self.cleaned_data['password']

        return md5(pwd)

    def clean_confirm_password(self):
        pwd = self.cleaned_data['password']

        confirm = md5(self.cleaned_data['confirm_password'])

        if pwd != confirm:
            raise ValidationError('两次密码输入不一致喵~')

        return confirm

class TaskModelForm(Bootstrap_model_form):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'detail': forms.TextInput
        }

class OrderModelForm(Bootstrap_model_form):
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['oid', 'admin'] # 去除一些不需要前端提交的数据项
        widgets = {

        }