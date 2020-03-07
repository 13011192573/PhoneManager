#!/usr/bin/env python
# -*- coding:utf-8 -*-
#__author__=v_zhangjunjie02
from django.shortcuts import render
from django.http import HttpResponse
from common.models import Users
from django.core.paginator import Paginator
from  datetime import datetime
#用户信息管理
def index(request,pIndex):
    '''浏览信息'''
    list=Users.objects.all()
    p=Paginator(list,10)
    if pIndex == '':
        pIndex = '1'
    pIndex=int(pIndex)
    list1=p.page(pIndex)
    plist=p.page_range
    context={'userslist':list1,'plist':plist,'pIndex':pIndex}
    return render(request,'myadmin/users/index.html',context)

def indexa(request,pIndex):
    '''浏览信息'''
    list=Users.objects.all()
    p=Paginator(list,10)
    if pIndex == '':
        pIndex = '1'
    pIndex=int(pIndex)
    list1=p.page(pIndex)
    plist=p.page_range
    context={'userslist':list1,'plist':plist,'pIndex':pIndex}
    return render(request,'myadmin/users/indexa.html',context)




def add(request):
    '''加载添加页面'''
    return render(request,'myadmin/users/add.html')


def insert(request):
    '''执行添加信息'''
    try:
        ob=Users()
        ob.username=request.POST['username']
        ob.name=request.POST['name']
        import hashlib
        m=hashlib.md5()
        m.update(bytes(request.POST['password'],encoding="utf8"))
        ob.password=m.hexdigest()
        ob.state=1
        ob.create_at=datetime.now()
        ob.update_at=datetime.now()
        ob.save()
        context={"info":"添加成功"}

    except Exception as err:

        print(err)
        context={"info":"添加失败"}
    return render(request,'myadmin/info.html',context)


def delete(request,uid):
    '''删除信息'''
    try:
        ob = Users.objects.get(id=uid)
        ob.delete()
        context = {"info": "删除成功"}
    except Exception as err:
        print(err)
        context={"info":"删除失败"}
    return render(request,'myadmin/info.html',context)

def edit(request,uid):
    '''加载编辑信息页面'''
    try:
        ob = Users.objects.get(id=uid)
        context = {"user": ob}
        return render(request, 'myadmin/users/edit.html', context)
    except Exception as err:
        context={"info":"没有要找到编辑信息"}
        return render(request,'myadmin/info.html',context)

def resetpassword(request,uid):
    '''加载重置密码表单'''
    try:
        ob = Users.objects.get(id=uid)
        context = {"user": ob}
        return render(request, 'myadmin/users/resetpd.html', context)
    except Exception as err:
        print(err)
        context={"info":"没有要找到编辑信息"}
        return render(request,'myadmin/info.html',context)

def updatepd(request,uid):
    '''执行重置密码'''
    try:
        ob = Users.objects.get(id=uid)
        import hashlib
        m = hashlib.md5()
        newpd=request.POST['newpassword']
        print(newpd)
        if newpd != None:
            m.update(bytes(newpd, encoding="utf8"))
            ob.password = m.hexdigest()
            ob.save()
            context = {"info": "修改成功"}
            return render(request, 'myadmin/info.html', context)
        else:
            context = {"info": "未输入密码"}
            return render(request, 'myadmin/info.html', context)

    except Exception as err:
        print(err)
        context = {"info": "修改失败"}
    return render(request,'myadmin/info.html',context)


def update(request,uid):
    '''执行编辑信息'''
    try:
        ob=Users.objects.get(id=uid)
        ob.name=request.POST['name']
        ob.state=request.POST['state']
        ob.update_at = datetime.now()
        ob.save()
        context={"info":"修改成功"}

    except Exception as err:

        print(err)
        context={"info":"修改失败"}
    return render(request,'myadmin/info.html',context)



