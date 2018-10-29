#coding=utf-8
from django.conf.urls import url

from archives import views

urlpatterns = [
    url(r'^student/',views.stu_info_view,name='student'),
    url(r'^register/',views.stu_school_register,name='register'),

]