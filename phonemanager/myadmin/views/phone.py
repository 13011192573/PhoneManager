#!/usr/bin/env python
# -*- coding:utf-8 -*-
#__author__=v_zhangjunjie02
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from common.models import Phone,Users
#from PIL import Image
from datetime import datetime
import time,json,os

#用户信息管理

def index(request,pIndex):
    '''获取手机信息'''
    mod=Phone.objects
    mywhere = []
    pkw = request.GET.get('phonekeyword',None)
    if pkw:
        list = mod.filter(name__contains=pkw)
        mywhere.append("phonekeyword=" + pkw)
    else:
        list = mod.filter()

    ukd = request.GET.get('userkeyword', None)
    if ukd:
        list = mod.filter(user__contains=ukd)
        mywhere.append("userkeyword=" + ukd)
    elif None:
        list = mod.filter()
    state = request.GET.get('state', '')
    if state != '':
        list = mod.filter(state=state)
        mywhere.append("state=" + state)

    sys =  request.GET.get('sys', '')
    if sys != '':
        list = list.filter(sys=sys)
        mywhere.append("sys=" + sys)

        # 执行分页处理
    pIndex = int(pIndex)
    page = Paginator(list, 8)  # 以5条每页创建分页对象
    maxpages = page.num_pages  # 最大页数
        # 判断页数是否越界
    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1:
        pIndex = 1
    list2 = page.page(pIndex)  # 当前页数据
    plist = page.page_range  # 页码数列表

    context = {'phonelist': list2, 'plist': plist, 'pIndex': pIndex,'mywhere':mywhere}

    return render(request, "myadmin/phone/index.html", context)

def indexa(request,pIndex):
    '''获取手机信息'''
    mod = Phone.objects
    mywhere = []
    pkw = request.GET.get('phonekeyword', None)
    if pkw:
        list = mod.filter(name__contains=pkw)
        mywhere.append("phonekeyword=" + pkw)
    else:
        list = mod.filter()

    nkw = request.GET.get('num',None)
    if nkw:
        list = mod.filter(phonenum__contains=nkw)
        mywhere.append("num=" + nkw)
    elif None:
        list=mod.filter()
    state = request.GET.get('state', '')
    if state != '':
        list = mod.filter(state=state)
        mywhere.append("state=" + state)

    sys = request.GET.get('sys', '')
    if sys != '':
        list = list.filter(sys=sys)
        mywhere.append("sys=" + sys)

        # 执行分页处理
    pIndex = int(pIndex)
    page = Paginator(list, 8)  # 以5条每页创建分页对象
    maxpages = page.num_pages  # 最大页数
    # 判断页数是否越界
    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1:
        pIndex = 1
    list2 = page.page(pIndex)  # 当前页数据
    plist = page.page_range  # 页码数列表

    context = {'phonelist': list2, 'plist': plist, 'pIndex': pIndex, 'mywhere': mywhere}
    return render(request, "myadmin/phone/indexa.html", context)



def add(request):

    return render(request,'myadmin/phone/add.html')


def insert(request):
    '''执行添加信息'''
    try:
        # 判断并执行图片上传，缩放等处理
        myfile = request.FILES.get("pic", None)
        if not myfile:
            return HttpResponse("没有上传文件信息！")
        # 以时间戳命名一个新图片名称
        filename = str(time.time()) + "." + myfile.name.split('.').pop()
        destination = open(os.path.join("./static/myadmin/img/", filename), 'wb+')
        for chunk in myfile.chunks():  # 分块写入文件
            destination.write(chunk)
        destination.close()

        # # 执行图片缩放
        # im = Image.open("./static/myadmin/img/" + filename)
        # # 缩放到75*75:
        # im.thumbnail((75, 75))
        # # 把缩放后的图像用jpeg格式保存:
        # im.save("./static/myadmin/img/s_" + filename, 'jpeg')

        # 获取商品信息并执行添加
        ob = Phone()
        ob.name = request.POST['name']
        ob.picname = filename
        ob.sys = 1
        ob.sysnum = request.POST['sysnum']
        ob.state = 1
        ob.phonenum=request.POST['phonenum']
        ob.save()
        context = {'info': '添加成功！'}
    except Exception as err:
        print(err)
        context = {'info': '添加失败！'}

    return render(request, "myadmin/info.html", context)


def delete(request,pid):
    '''删除信息'''
    try:
        # 获取被删除商品信的息量，先删除对应的图片
        ob = Phone.objects.get(id=pid)
        # 执行图片删除
        os.remove("./static/myadmin/img/" + ob.picname)
        # 执行商品信息的删除
        ob.delete()
        context = {'info': '删除成功！'}
    except Exception as err:
        print(err)
        context = {'info': '删除失败！'}
    return render(request, "myadmin/info.html", context)

def edit(request,pid):
    '''加载编辑信息页面'''
    try:
        # 获取要编辑的信息
        ob = Phone.objects.get(id=pid)


        context = {'phone': ob}

        return render(request, "myadmin/phone/edit.html", context)
    except Exception as err:
        print(err)

        context = {'info': '没有找到要修改的信息！'}
    return render(request, "myadmin/info.html", context)

def update(request,pid):
    try:
        b = False
        oldpicname = request.POST['oldpicname']
        if None != request.FILES.get("pic"):
            myfile = request.FILES.get("pic", None)
            if not myfile:
                return HttpResponse("没有上传文件信息！")
            # 以时间戳命名一个新图片名称
            filename = str(time.time()) + "." + myfile.name.split('.').pop()
            destination = open(os.path.join("./static/myadmin/img/", filename), 'wb+')
            for chunk in myfile.chunks():  # 分块写入文件
                destination.write(chunk)
            destination.close()
            # # 执行图片缩放
            # im = Image.open("./static/myadmin/img/" + filename)
            #
            # im.thumbnail((75, 75))
            # # 把缩放后的图像用jpeg格式保存:
            # im.save("./static/myadmin/img/s_" + filename, 'jpeg')
            b = True
            picname = filename
        else:
            picname = oldpicname
        ob = Phone.objects.get(id=pid)
        ob.name = request.POST['name']
        ob.picname = picname
        ob.sys = request.POST['sys']
        ob.state = 1
        ob.sysnum=request.POST['sysnum']
        ob.phonenum=request.POST['phonenum']
        ob.save()
        context = {'info': '修改成功！'}
        if b:
            os.remove("./static/myadmin/img/" + oldpicname)  # 执行老图片删除
    except Exception as err:
        print(err)
        context = {'info': '修改失败！'}
        if b:
            os.remove("./static/myadmin/img/" + picname)  # 执行新图片删除
    return render(request, "myadmin/info.html", context)

def borrow(request,pid):
    try:
        oc=Users.objects.get(id=request.session['adminuser']['id'])
        ob = Phone.objects.get(id=pid)
        ob.state=2
        ob.create_at=datetime.now()
        ob.update_at=None
        print(request.session['adminuser'])
        ob.user=request.session['adminuser']['name']
        ob.backuser=None
        oc.cclicknum+=1
        oc.save()
        ob.save()
        context={"info": "借用成功，别忘了用完要及时释放哦"}

    except Exception as err:
        print(err)
        context = {"info": "借用失败,再试一次可能会成功哦"}
    return render(request,"myadmin/info.html",context)

def back(request,pid):
    try:
        oc = Users.objects.get(id=request.session['adminuser']['id'])
        ob = Phone.objects.get(id=pid)
        ob.state=1
        ob.update_at=datetime.now()
        ob.user=''
        ob.backuser=request.session['adminuser']['name']
        oc.cclicknum-=1
        oc.save()
        ob.save()
        context={"info": "归还成功，别忘了放到机架上哈"}
    except Exception as err:
        print(err)
        context = {"info": "归还失败，再试一次可能会成功哦"}
    return render(request,'myadmin/info.html',context)
