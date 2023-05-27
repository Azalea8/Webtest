from django.urls import path
from app01 import views

urlpatterns = [
  path('test/', views.test),
  path('', views.test1),
  path('news/', views.news),
  path('something/', views.something),
  path('login/', views.login),
  path('orm/', views.orm),
  path('info_list/', views.info_list),
  path('info_add/', views.info_add),
  path('info_delete/', views.info_delete),
]