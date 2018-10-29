#coding=utf-8
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from login.models import Clazz, Stu, StuRegister


# 学生信息注册
def stu_info_view(request):
    if request.method == 'GET':
        # 根据班级名称查询班级
        clazzs = Clazz.objects.all()
        stus = Stu.objects.all()
        return render(request,'stu_info.html',{'clazzs':clazzs,'stus':stus,})
    else:
        #获取录入数据
        clazz = request.POST.get('clazz', '')
        cls = Clazz.objects.get(cls_name=clazz)#获取班级表信息
        political = request.POST.get('political', '')
        id = request.POST.get('id', '')
        id = int(id)#字符串转数据库int型
        name = request.POST.get('name', '')
        gender = request.POST.get('gender', '')
        healthy = request.POST.get('healthy', '')
        id_num = request.POST.get('id_num', '')
        birth = request.POST.get('birth', '')
        nation = request.POST.get('nation', '')
        age = request.POST.get('age', '')
        age = int(age)
        addr = request.POST.get('addr', '')
        phone = request.POST.get('phone', '')
        # 存入学生数据库
        try:
            Stu.objects.create(stu_id=id,clazz=cls,stu_gender=gender,
                               stu_id_num=id_num,stu_addr=addr,stu_political=political,
                               stu_healthy=healthy,stu_name=name,stu_phone=phone,
                               stu_age=age,stu_birthday=birth,stu_nation=nation)
            cue = '学生信息注册成功'
            return render(request,'cue.html',{'cue':cue,})
        except:
            cue = '学生信息注册失败'
            return render(request, 'cue.html', {'cue': cue,})

# 学生入校登记
def stu_school_register(request):
    if request.method == 'GET':
        return render(request, 'stu_school_register.html')
    else:
        if request.POST.get('submit', '') == '确定':
            id = request.POST.get('id','')
            id = int(id)
            stu = Stu.objects.get(stu_id=id)
            return render(request,'stu_school_register2.html',{'stu':stu})
        #点提交获取数据存入数据库
        elif request.POST.get('submit', '') == '提交':
            name = request.POST.get('name','')
            stu = Stu.objects.get(stu_name=name)
            clazz = request.POST.get('clazz', '')
            cls = Clazz.objects.get(cls_name=clazz)
            major = request.POST.get('major', '')
            enrollment = request.POST.get('enrollment','')
            recommender = request.POST.get('recommender','')
            score = request.POST.get('score','')
            StuRegister.objects.create(stu=stu,clazz=cls,stu_major=major,stu_recommender=recommender
                                       ,stu_enrollment=enrollment,stu_score=score,sr_id=stu.stu_id)
            cue = '提交成功'
            return render(request, 'cue.html', {'cue': cue})#为空都报错，需完善
        #点重置返回初始页
        elif request.POST.get('submit','') == '重置':#类型写submit防止冲突
            return render(request, 'stu_school_register.html')