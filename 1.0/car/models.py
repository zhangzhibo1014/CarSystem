from django.db import models

# Create your models here.
#用户基本信息表
class userinfo(models.Model):
    id = models.AutoField(primary_key=True)     #id
    name = models.CharField(max_length=10)      #姓名
    sex = models.CharField(max_length=1)        #性别
    job = models.CharField(max_length=50)       #职业
    idcard = models.CharField(max_length=20)    #身份证号码
    phone = models.CharField(max_length=20)     #联系方式
    username = models.CharField(max_length=20)  #用户名
    password = models.CharField(max_length=20)  #密码
    power_id = models.IntegerField()            #权限id

#权限表
class power(models.Model):
    power_id = models.IntegerField()                #权限id
    power_name = models.CharField(max_length=20)    #权限名


#操作日志表
class log(models.Model):
    id = models.AutoField(primary_key=True)             # 编号
    operation = models.CharField(max_length=200)        # 操作
    operation_time = models.DateTimeField()             # 操作时间
    ip_address = models.CharField(max_length=20)        # ip地址


#收费记录表
class charge(models.Model):
    plate_number = models.CharField(max_length=20, primary_key=True)    # 车牌号码
    charge_type = models.CharField(max_length=20)                       # 收费类型
    charge_time = models.DateTimeField()                                # 收费时间
    collector = models.CharField(max_length=20)                         # 操作人


#收费金额表
class chage_money(models.Model):
    id = models.AutoField(primary_key=True)                             # 编号
    charge_type = models.CharField(max_length=20)                       # 收费类型
    total_money = models.DecimalField(max_digits=6, decimal_places=2)   # 收费金额
    charge_time = models.DateTimeField()                                # 收费时间


#图片信息表
class images(models.Model):
    id = models.AutoField(primary_key=True)                 # 编号
    entry_image = models.BinaryField(null=True)             # 进入图片
    exit_image = models.BinaryField(null=True)              # 离开图片
    plate_number = models.CharField(max_length=20)          # 车牌号码


#黑名单
class blacklist(models.Model):
    plate_number = models.CharField(max_length=20, primary_key=True)
    black_time = models.DateField()
    vlolation_info = models.CharField(max_length=200, null=True)


#收费标准表
class charge_standard(models.Model):
    id = models.AutoField(primary_key=True)                             # 编号
    hour_money = models.DecimalField(max_digits=5, decimal_places=2)    # 每小时金额/元
    day_money = models.DecimalField(max_digits=5, decimal_places=2)     # 每天金额/元
    cross_money = models.DecimalField(max_digits=5, decimal_places=2)   # 穿行金额/元
    able = models.IntegerField()                                        # 是否可用


#校园常驻车辆
class car_school(models.Model):
    plate_number = models.CharField(max_length=20, primary_key=True)    # 车牌号码
    name = models.CharField(max_length=10)                              # 姓名
    sex = models.CharField(max_length=1)                                # 性别
    word_number = models.CharField(max_length=20)                       # 工作编号
    idcard = models.CharField(max_length=20)                            # 身份证号码
    phone = models.CharField(max_length=20)                             # 联系方式
    partment_id = models.IntegerField()                                 # 院系id


#院系信息表
class partment(models.Model):
    partment_id = models.IntegerField()                                 # 院系id
    partment_name = models.CharField(max_length=20)                     # 院系名称


#车辆信息表
class car(models.Model):
    plate_number = models.CharField(max_length=20, primary_key=True)        # 车牌号码
    in_date = models.DateTimeField()                                        # 进入时间
    out_date = models.DateTimeField(null=True)                              # 离开时间
    stay_date = models.IntegerField(null=True)                              # 在校时间
    money = models.DecimalField(max_digits=6,decimal_places=2,null=True)    # 金额
    car_type = models.CharField(max_length=20)                              # 车辆类型
    enter_info = models.CharField(max_length=20)                            # 入口信息
    exit_info = models.CharField(max_length=20,null=True)                   # 出口信息


#用户在线表
class online(models.Model):
    username = username = models.CharField(max_length=20)                   # 用户名
    login_time = models.DateTimeField()                                     # 登录时间


#车牌表
class plate(models.Model):
    id = models.AutoField(primary_key=True)                                 # 编号
    plate_number = models.CharField(max_length=20)                          # 车牌号码
