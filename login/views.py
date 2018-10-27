# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from login.models import User


def login_view(request):
    # return HttpResponse('123')
    if request.method == 'GET':
        return render(request, 'login.html')
    #获取用户数据
    else:
        uname = request.POST.get('uname','')
        pwd = request.POST.get('pwd','')
        # 遍历用户数据库匹配
        if uname and pwd:
            users = User.objects.filter(user_name=uname,user_password=pwd)
            #登陆成功用session记住用户
            if users:
                for use in users:
                    uid = use.user_id
                    # if uid < 5:
                    #     # del request.session['uname']
                    #     request.session['uname'] = '管理员'
                    #     request.session.set_expiry(60 * 60 * 24 * 3)
                    #     return render(request, 'base.html')
                    # else:
                        # del request.session['uname']
                    request.session['uname'] = uname
                    request.session.set_expiry(60 * 60 * 24 * 3)
                    return  redirect('/index/')
            else:
                return render(request, 'relogin.html')


def index_view(request):
    return render(request, 'index.html')