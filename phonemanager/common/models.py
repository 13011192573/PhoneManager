
from django.db import models
from datetime import  datetime

#用户信息模型
class Users(models.Model):
    username = models.CharField(max_length=32)
    name = models.CharField(max_length=16)
    password = models.CharField(max_length=32)
    cclicknum = models.IntegerField(default=0)
    qclicknum = models.IntegerField(default=0)
    state = models.IntegerField(default=1)
    create_at = models.DateTimeField(default=datetime.now)  # 创建时间
    update_at = models.DateTimeField(default=datetime.now)  # 修改时间

    def toDict(self):
        return {'id':self.id,'username':self.username,'name':self.name,'password':self.password,'cclicknum':self.cclicknum,'qclicknum':self.qclicknum,'state':self.state,'create_at':self.create_at.strftime('%Y-%m-%d %H:%M:%S'),'update_at':self.update_at.strftime('%Y-%m-%d %H:%M:%S')}
        # , 'addtime':self.addtime

    class Meta:
        db_table = "users"  # 更改表名



#商品信息模型
class Phone(models.Model):
    name = models.CharField(max_length=32)
    picname = models.CharField(max_length=255)
    sys = models.IntegerField(default=1)
    sysnum = models.CharField(max_length=32)
    state = models.IntegerField(default=1)
    user = models.CharField(max_length=32)
    backuser = models.CharField(max_length=30)
    create_at = models.DateTimeField()  # 创建时间
    update_at = models.DateTimeField()  # 修改时间
    phonenum = models.CharField(max_length=30)

    def toDict(self):
        return {'id':self.id,'name':self.name,'sys':self.sys,'sysnum':self.sysnum,'state':self.state,'user':self.user,'create_at':self.create_at.strftime('%Y-%m-%d %H:%M:%S'),'update_at':self.update_at.strftime('%Y-%m-%d %H:%M:%S'),'phonenum':self.phonenum}

    class Meta:
        db_table = "phone"  # 更改表名


