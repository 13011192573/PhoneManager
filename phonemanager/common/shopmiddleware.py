from django.shortcuts import redirect
from django.core.urlresolvers import reverse
import re

class ShopMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.
        print("hdfhhdshhsad ")

    def __call__(self, request):
        
        #获取当前请求路径
        path = request.path
        print("mycall..."+path)

        # 后台请求路由判断
        # 定义网站后台不用登录也可访问的路由url
        urllist = ['/myadmin/login','/myadmin/dologin','/myadmin/logout','/myadmin/verify','/myadmin/register','/myadmin/doregister']
        # 判断当前请求是否是访问网站后台,并且path不在urllist中
        if re.match(r"^/myadmin",path) and (path not in urllist):
            # 判断当前用户是否没有登录
            if "adminuser" not in request.session:
                # 执行登录界面跳转
                return redirect(reverse('myadmin_login'))

        response = self.get_response(request)

        return response