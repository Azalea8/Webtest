from django.urls import path
from app02.views import depart, user, pretty_num, admin, account, task

urlpatterns = [

    path('login/', account.login),
    path('logout/', account.logout),


    path('admin/list/', admin.admin_list),
    path('admin/add/', admin.admin_add),
    path('admin/<int:nid>/delete/', admin.admin_delete),
    path('admin/<int:nid>/edit/', admin.admin_edit),

    # 部门管理
    path('depart/list/', depart.depart_list),
    path('depart/add/', depart.depart_add),
    path('depart/delete/', depart.depart_delete),
    path('depart/<int:nid>/edit/', depart.depart_edit),

    # 用户管理
    path('user/list/', user.user_list),
    path('user/add/', user.user_add),
    path('user/model_add/', user.user_model_add),
    path('user/<int:nid>/edit/', user.user_edit),
    path('user/<int:nid>/delete/', user.user_delete),

    # 靓号
    path('prettynum/list/', pretty_num.pretty_list),
    path('prettynum/add/', pretty_num.pretty_add),
    path('prettynum/<int:nid>/delete/', pretty_num.pretty_delete),
    path('prettynum/<int:nid>/edit/', pretty_num.pretty_edit),

    path('task/list/', task.task_list),
]