# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def login_view(request):
    # return HttpResponse('123')
    return render(request,'homepages.html')