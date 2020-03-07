#!/usr/bin/env python
# -*- coding:utf-8 -*-
#__author__=v_zhangjunjie02
from django.conf.urls import url


from myadmin.views import index,users,phone

urlpatterns = [
    # 后台首页
    url(r'^$', index.index, name="myadmin_index"),

    #用户注册路由
    url(r'^register$', index.register, name="myadmin_register"),
    url(r'^doregister$', index.doregister, name="myadmin_doregister"),
    #用户登录和退出路由配置
    url(r'^login$', index.login, name="myadmin_login"),
    url(r'^dologin$', index.dologin, name="myadmin_dologin"),
    url(r'^logout$', index.logout, name="myadmin_logout"),
    #url(r'^verify$', index.verify, name="myadmin_verify"),  # 验证码


    url(r'^users/(?P<pIndex>[0-9]+)$', users.index, name='myadmin_users_index'),
    url(r'^usersa/(?P<pIndex>[0-9]+)$', users.indexa, name='myadmin_usersa_index'),
    url(r'^users/resetpd/(?P<uid>[0-9]+)$', users.resetpassword, name='myadmin_users_resetpd'),
    url(r'^users/updatepd/(?P<uid>[0-9]+)$', users.updatepd, name='myadmin_pd_update'),
    url(r'^users/add$', users.add, name='myadmin_users_add'),
    url(r'^users/insert$', users.insert, name='myadmin_users_insert'),
    url(r'^users/del/(?P<uid>[0-9]+)$', users.delete, name='myadmin_users_del'),
    url(r'^users/edit/(?P<uid>[0-9]+)$', users.edit, name='myadmin_users_edit'),
    url(r'^users/update/(?P<uid>[0-9]+)$', users.update, name='myadmin_users_update'),



    url(r'^phone/(?P<pIndex>[0-9]+)$', phone.index, name='myadmin_phone_index'),
    url(r'^managephone/(?P<pIndex>[0-9]+)$', phone.indexa, name='myadmin_managephone_index'),
    url(r'^phone/add$', phone.add, name='myadmin_phone_add'),
    url(r'^phone/insert$', phone.insert, name='myadmin_phone_insert'),
    url(r'^phone/del/(?P<pid>[0-9]+)$', phone.delete, name='myadmin_phone_del'),
    url(r'^phone/edit/(?P<pid>[0-9]+)$', phone.edit, name='myadmin_phone_edit'),
    url(r'^phone/update/(?P<pid>[0-9]+)$', phone.update, name='myadmin_phone_update'),

    #机器借还路由
    url(r'^phone/borrow/(?P<pid>[0-9]+)$', phone.borrow, name='myadmin_phone_borrow'),
    url(r'^phone/back/(?P<pid>[0-9]+)$', phone.back, name='myadmin_phone_back'),














]
