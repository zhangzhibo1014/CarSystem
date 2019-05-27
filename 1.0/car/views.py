from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponseRedirect, HttpResponse
import time
from django.db.models import *
from django.db import connection
import django
from .models_views import *
import json
import datetime
import arrow
# Create your views here.

# 登陆
def login(requset):
    if requset.method == "POST":  # 判断表单是否是POST
        username = requset.POST['username']  # 获取表单内输入的用户名
        password = requset.POST['password']  # 获取表单内输入的密  码
        try:
            ret = userinfo.objects.get(username=username)
        except:
            return render(requset, 'login.html', {'status': '用户名或密码错误，请重新登陆'})
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 获取本地时间
        if len(online.objects.filter(username=username)) > 0:  # 判断表内是否有 ，有则更新，无则添加
            online.objects.filter(username=username).update(login_time=now)
        else:
            online.objects.create(username=username, login_time=now)
        if ret.username == username and ret.password == password and ret.power_id == -1:  # 根据用户名，密码，权限来跳转
            requset.session['admin'] = username  # 创建session对象 用来保存用户名
            return redirect("/admin/index.html")
        elif ret.username == username and ret.password == password and ret.power_id == 0:
            requset.session['operator'] = username  # 创建session对象 用来保存用户名
            return redirect("/operator/index.html")
        else:
            return render(requset, 'login.html', {'status': '用户名或密码错误，请重新登陆'})
    return render(requset, 'login.html')


# 管理员 - 首页
def adminIndex(request):
    session_name = request.session.get('admin')  # 获取管理员的名字
    now = datetime.datetime.now().strftime('%Y-%m-%d')  # 获取本地时间
    ret = car.objects.filter(in_date__date=now)  # 查询car表中当日的所有记录
    count = len(ret)  # 查询表中数据个数
    res = car.objects.filter(in_date__date=now, car_type='社会车辆')  # 查询当前时间，车辆类型为社会车辆的数据
    nows = len(res)  # 查询满足条件的数据个数
    ret1 = car.objects.all().order_by('in_date').reverse()  # 查询表中所有记录
    cursor = connection.cursor()  # 使用自定义sql
    cursor.execute("select sum(money) from car_car where in_date like '%s'" % ("%" + now + "%"))  # 查询总金额
    row = cursor.fetchone()
    ret2 = online.objects.all()  # 查询online表中所有记录
    person_count = len(ret2)  # 查询表的数据量个数
    context = {  # 记录保存传入界面的数据
        'count': count,
        'nows': nows,
        'lists': ret1,
        'session_name': session_name,
        'money': row[0],
        'person_count': person_count,
    }
    return render(request, 'admin/index.html', context)


# 管理员 - 黑名单
def adminBlackList(request):
    session_name = request.session.get('admin')  # 获取管理员的名字
    ret = blacklist.objects.all()
    context = {
        'blacklists' : ret,
        'session_name' : session_name
    }
    return render(request, 'admin/blackList.html', context)


# 管理员 - 黑名单 - 新增黑名单
def blacklist_add(request):
    if request.method == "POST":
        plate_number = request.POST['plate_number']
        in_time = request.POST['in_time']
        info = request.POST['info']
        ret = blacklist.objects.create(plate_number=plate_number, black_time=in_time, vlolation_info=info)
        if ret != None:
            return redirect('admin/blackList.html')
        else:
            return render(request, 'admin/blackList.html')


# 管理员 - 黑名单 - 移出黑名单
def move_temp(request):
    if request.is_ajax():
        plate_number = request.POST['plate_number']
        blacklist.objects.filter(plate_number=plate_number).delete()
        return HttpResponse()
    else :
        return render(request, 'admin/blackList.html')


# 管理员 - 当日车辆信息
def adminCarDay(request):
    session_name = request.session.get('admin')  # 获取管理员的名字
    now = datetime.datetime.now().strftime('%Y-%m-%d')
    ret = car.objects.filter(in_date__date=now, out_date__isnull=False).order_by('in_date')
    context = {
        'carDayLists' : ret,
        'session_name' : session_name,
    }
    return render(request, 'admin/carDay.html',context)


# 管理员 - 车辆历史信息
def adminCarHistory(request):
    session_name = request.session.get('admin')  # 获取管理员的名字
    ret = car.objects.filter(out_date__isnull=False).order_by('in_date').reverse()
    context  = {
        'carHistory' : ret,
        'session_name' : session_name,
    }
    return render(request, 'admin/carHistory.html', context)


# 管理员 - 实时车辆信息
def adminCarReal(request):
    session_name = request.session.get('admin')  # 获取管理员的名字
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    utc = arrow.utcnow()  # 获取现在的utc时间
    local = utc.to('local')  # 将utc时间转换为本地时间
    local_zero = local.replace(hour=0, minute=0, second=0)
    today = local_zero.format("YYYY-MM-DD HH:mm:ss")  # 输出当天零点时间
    # print(now)
    ret = car.objects.filter(Q(out_date__isnull=True) & Q(in_date__lte=now) & Q(in_date__gt=today)).order_by('in_date')
    context = {
        'realLists' : ret,
        'session_name' : session_name,
    }
    return render(request, 'admin/carReal.html', context)


# 管理员 - 校园常驻车辆
def adminCarSchool(request):
    session_name = request.session.get('admin')  # 获取管理员的名字
    ret = car_school_view.objects.all()  # 获取视图内的数据
    partments = partment.objects.values_list('partment_name')
    context = {
        'lists' : ret,
        'session_name' : session_name,
        'partments' : partments,
    }
    return render(request, 'admin/carSchool.html', context)


# 管理员 - 校园常驻车辆 - 添加车辆信息
def carschool_add(request):
    if request.method == "POST":
        username = request.POST['username']
        sex = request.POST['sex']
        work_number = request.POST['worknumber']
        plate_number = request.POST['platenumber']
        phone = request.POST['tel']
        partment_name = request.POST['partment_name']
        idcard = request.POST['idcard']
        ret = partment.objects.filter(partment_name=partment_name).values('partment_id')
        partment_id = ret[0]["partment_id"]
        ret1 = car_school.objects.create(plate_number=plate_number, name=username, sex=sex, word_number=work_number, idcard=idcard, phone=phone, partment_id=partment_id)
        if ret1 != None:
            return redirect('/admin/carSchool.html')
        else:
            return render(request, 'admin/carSchool.html')


# 管理员 - 校园常驻车辆 - 移动到黑名单
def toBlackList(request):
    if request.is_ajax():
        now = datetime.datetime.now().strftime('%Y-%m-%d')
        names = request.POST.getlist('name')
        message = "无"
        count = 0
        for i in range(len(names)):
            plate_number = names[i]
            car_school.objects.filter(plate_number=plate_number).delete()
            length1 = blacklist.objects.create(plate_number=plate_number, black_time=now, vlolation_info=message)
            if length1 != None:
                count += 1
        if count != 0:
            ret = {"data" : 1}
        else :
            ret = {"data" : 0}
        return HttpResponse(json.dumps(ret))
    else:
        return render(request, 'admin/carSchool.html')


# 管理员 - 校园常驻车辆 - 转为临时车
def toTemp(request):
    if request.is_ajax():
        names = request.POST.getlist('name')
        for i in range(len(names)):
            plate_number = names[i]
            car_school.objects.filter(plate_number=plate_number).delete()
        return HttpResponse()
    else:
        return render(request, 'admin/carSchool.html')


# 管理员 - 收费金额
def adminChargeMoney(request):
    session_name = request.session.get('admin')  # 获取管理员的名字
    now = datetime.datetime.now().strftime('%Y-%m-%d')
    today = datetime.date.today()
    month = today.replace(day=1)    #获取每月第一天
    next_month = month.replace(day=28) + datetime.timedelta(days=4) #获取下个月第一天
    this_month = month.strftime("%Y-%m")
    year = datetime.datetime.now().year
    ret = chage_money.objects.filter(charge_time__date=now).values_list('charge_type').annotate(Sum('total_money')) # 获取每日金额
    dict_day = {
        '微信':0,
        '支付宝': 0,
        '现金' : 0,
    }
    for i in ret:
        dict_day[i[0]] = float(i[1])
    print(dict_day)
    ret1 = chage_money.objects.filter(charge_time__gt=month, charge_time__lt=next_month).values_list('charge_type').annotate(Sum('total_money')) # 获取每月金额
    dict_month = {
        '微信': 0,
        '支付宝': 0,
        '现金': 0,
    }
    for i in ret1:
        dict_month[i[0]] = float(i[1])
    # print(dict_month)
    ret2 = chage_money.objects.filter(charge_time__year=year).values_list('charge_type').annotate(Sum('total_money')) # 获取本年金额
    dict_year = {
        '微信': 0,
        '支付宝': 0,
        '现金': 0,
    }
    for i in ret2:
        dict_year[i[0]] = float(i[1])
    # print(dict_year)
    context = {
        'session_name' : session_name,
        'moneyList' : json.dumps(dict_day),
        'now' : now,
        'money_month' : json.dumps(dict_month),
        'this_month' : this_month,
        'year' : year,
        'money_year' : json.dumps(dict_year),
    }
    return render(request, 'admin/chargeMoney.html', context)


# 管理员 - 收费记录
def adminChargeRecord(request):
    session_name = request.session.get('admin')  # 获取管理员的名字
    ret = charge_money_view.objects.all().order_by('charge_time').reverse()
    context = {
        'session_name' : session_name,
        'recordLists' : ret,
    }
    return render(request, 'admin/chargeRecord.html', context)


# 管理员 - 收费标准
def adminChargeStandard(request):
    session_name = request.session.get('admin')  # 获取管理员的名字
    ret = charge_standard.objects.all()
    ret1 = charge_standard.objects.values('id','able')
    dict = {}
    for i in ret1:
        dict2 = {i['id']:i['able']}
        dict.update(dict2)
    context = {
        'chargeStandardLists' : ret,
        'session_name' : session_name,
        'dict' : json.dumps(dict),
    }
    return render(request, 'admin/chargeStandard.html', context)


#管理员 - 收费标准 - 是否启用
def toEnable(request):
    if request.is_ajax():
        cid = request.POST['e']
        ables = request.POST['able']
        if ables == "0":
            charge_standard.objects.filter(id=int(cid)).update(able=0)
        if ables == "1":
            charge_standard.objects.filter(id=int(cid)).update(able=1)
        return HttpResponse()
    else :
        return render(request, 'admin/chargeStandard.html')


# 管理员 - 收费标准 - 删除
def delete_chargestandard(request):
    if request.is_ajax():
        e = request.POST['e'];
        charge_standard.objects.filter(id=e).delete()
        return  HttpResponse();
    else:
        return render(request, 'admin/chargeStandard.html')


# 管理员 - 收费标准 - 新增
def add_chargestandard(request):
    if request.method == "POST":
        hourMoney = request.POST['hourMoney']
        dayMoney = request.POST['dayMoney']
        crossMoney = request.POST['crossMoney']
        ret = charge_standard.objects.create(hour_money=hourMoney, day_money=dayMoney, cross_money=crossMoney, able=0)
        if ret != None:
            return redirect('admin/chargeStandard.html')
        else :
            return render(request,'admin/chargeStandard.html')


# 管理员 - 操作日志
def adminLog(request):
    session_name = request.session.get('admin')  # 获取管理员的名字
    # import socket
    ip = get_ip(request)
    # print(ip)
    now = datetime.datetime.now().strftime('%Y-%m-%d')
    makeLog(ip)
    ret = log.objects.all().order_by('operation_time').reverse()
    context = {
        'session_name' : session_name,
        'ip' : ip,
        'now' : now,
        'logs' : ret,
    }
    return render(request, 'admin/log.html', context)

def get_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]#所以这里是真实的ip
    else:
        ip = request.META.get('REMOTE_ADDR')#这里获得代理ip
    return ip


def makeLog(ip):
    import pymysql
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "root", "hdcar")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 行为字典
    Behavior_dict = {
        'login.html': '用户登陆',
        'admin/index.html': '管理员查看首页信息',
        'admin/blackList.html': '管理员查看黑名单信息',
        'admin/carDay.html': '管理员查看当日车辆信息',
        'admin/carHistory.html': '管理员查看车辆历史信息',
        'admin/carReal.html': '管理员查看车辆实时信息',
        'admin/carSchool.html': '管理员查看校园常驻车辆信息',
        'admin/chargeMoney.html': '管理员查看收费金额信息',
        'admin/chargeRecord.html': '管理员查看收费记录信息',
        'admin/chargeStandard.html': '管理员查看收费标准',
        'admin/log.html': '管理员查看操作日志信息',
        'admin/passwordEdit.html': '管理员查看密码修改',
        'admin/userManage.html': '管理员查看用户信息',
        'carschool_add': '管理员添加校园常驻车辆',
        'toBlackList': '管理员将校园常驻车辆移动到黑名单',
        'toTemp': '管理员将校园常驻车辆转为临时车',
        'blacklist_add': '管理员添加车辆黑名单',
        'move_temp': '管理员移出车辆黑名单',
        'toEnable': '管理员启用或关闭收费标准',
        'delete_chargestandard': '管理员删除收费标准',
        'add_chargestandard': '管理员添加收费标准',
        'add_userinfo': '管理员添加用户',
        'delete_userinfo': '管理员删除用户',
        'update_userinfo': '管理员修改用户',
        'editpassword': '管理员进行密码修改',
        'operator/index.html': '操作员查看首页信息',
        'operator/blackList.html': '操作员查看黑名单信息',
        'operator/carDay.html': '操作员查看当日车辆信息',
        'operator/carHistory.html': '操作员查看查看车辆历史信息',
        'operator/carReal.html': '操作员查看车辆实时信息',
        'operator/chargeRecord.html': '操作员查看收费记录',
        'operator/passwordEdit.html': '操作员查看密码修改',
        'operator_blacklist_add': '操作员添加黑名单',
        'operator_editpassword': '操作员进行密码修改',
        'operator_conCharges' : '操作员进行收费放行',
    }
    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("SELECT content,time from log")
    data = cursor.fetchall()

    # print(data)
    ip = ip
    for j in data:  # 遍历列表中每一句内容
        k = j[0]
        time = j[1]
        for i in Behavior_dict:  # 遍历翻译字典中每一个key
            if i in k:  # 判断字典中key是否在字符串k中
                OperationInformation = Behavior_dict[i]  # 操作信息
                # print(OperationInformation, time,ip)
                sql = "INSERT INTO car_log(operation,operation_time,ip_address)VALUES (%s,%s,%s)"
                cursor.execute(sql, ( OperationInformation, time, ip))  # 传值
                db.commit()  # 提交事务
                sql = "delete from log"
                cursor.execute(sql)
                db.commit()
    # 关闭数据库连接
    db.close()


# 管理员 - 密码修改
def adminPasswordEdit(request):
    session_name = request.session.get('admin')  # 获取管理员的名字
    context = {
        'session_name' : session_name,
    }
    return render(request, 'admin/passwordEdit.html', context)


# 管理员 - 修改密码
def editpassword(request):
    if request.method == "POST":
        username = request.POST['this_username']
        password = request.POST['this_password']
        new_password = request.POST['new_password']
        try:
            ret = userinfo.objects.get(username=username, password=password)
            userinfo.objects.filter(username=username, password=password).update(password=new_password)
            return redirect('/login.html')
        except:
            return render(request, 'admin/passwordEdit.html', {"status": "输入的用户名或密码错误"})



# 管理员 - 用户管理
def adminUserManage(request):
    session_name = request.session.get('admin')  # 获取管理员的名字
    ret = user_view.objects.all()
    context = {
        'users' : ret,
        'session_name' : session_name,
    }
    return render(request, 'admin/userManage.html', context)


#管理员 - 用户管理 - 添加
def add_userinfo(request):
    if request.method == "POST":
        name = request.POST['name']
        sex = request.POST['sex']
        job = request.POST['job']
        idcard = request.POST['idcard']
        phone = request.POST['phone']
        quanxian = request.POST['quanxian']
        username = request.POST['username']
        password = request.POST['password']
        powerid = 1000
        if quanxian == "管理员":
            powerid = -1
        else :
            powerid = 0
        ret = userinfo.objects.create(name=name,sex=sex,job=job,idcard=idcard,phone=phone,power_id=powerid)
        if ret != None:
            return redirect('admin/userManage.html')
        else :
            return render(request, 'admin/userManage.html')


# 管理员 - 用户管理 - 删除
def delete_userinfo(request):
    if request.is_ajax():
        names = request.POST.getlist('name')
        for i in range(len(names)):
            id = names[i]
            userinfo.objects.filter(id=id).delete()
        return HttpResponse()
    else:
        return render(request, 'admin/carSchool.html')


# 管理员 - 用户管理 - 修改
def update_userinfo(request):
    if request.method == "POST":
        phone = request.POST['phone_update']
        quanxian = request.POST['quanxian_update']
        idcard = request.POST['idcard_update']
        if quanxian == '管理员':
            powerid = -1
        else :
            powerid = 0
        userinfo.objects.filter(idcard=idcard).update(phone=phone,power_id=powerid)
        return redirect('admin/userManage.html')
    else :
        return render(request, 'admin/userManage.html')



# 操作员 - 首页
'''
存在问题;  
1.没有车辆会出错，页面无法加载
2.局部刷新问题
'''
def operatorIndex(request):
    session_name = request.session.get('operator')  # 获取管理员的名字
    count = plate.objects.all().count()
    tojump = 0
    if count > 1:
        cursor = connection.cursor()  # 使用自定义sql
        cursor.execute("select plate_number from car_plate order by id desc")  # 查询总金额
        row = cursor.fetchone()
        plate_number = row[0]
        cursor = connection.cursor()  # 使用自定义sql
        cursor.execute("select plate_number from car_plate order by id")  # 查询总金额
        row = cursor.fetchone()
        last = row[0]
        # print(plate_number, last)
        cursor = connection.cursor()  # 使用自定义sql
        cursor.execute("select entry_image,exit_image from car_images where plate_number = '%s'" % (plate_number))  # 查询总金额
        row = cursor.fetchone()
        f1 = open('static/images/in.png', 'wb')
        f1.write(row[0])
        f2 = open('static/images/out.png', 'wb')
        f2.write(row[1])
        f1.close()
        f2.close()
        cursor = connection.cursor()  # 使用自定义sql
        cursor.execute("select * from car_car where plate_number = '%s'" % (plate_number))  # 查询总金额
        row = cursor.fetchone()
        in_date = row[1]
        in_date = in_date.strftime("%Y-%m-%d %H:%M:%S")
        out_date = row[2]
        out_date = out_date.strftime("%Y-%m-%d %H:%M:%S")
        money = row[4]
        in_info = row[6]
        out_info = row[7]
        plate.objects.filter(plate_number=last).delete()
        tojump = 1
    else :
        cursor = connection.cursor()  # 使用自定义sql
        cursor.execute("select plate_number from car_plate")  # 查询总金额
        row = cursor.fetchone()
        plate_number = row[0]
        cursor = connection.cursor()  # 使用自定义sql
        cursor.execute(
            "select entry_image,exit_image from car_images where plate_number = '%s'" % (plate_number))  # 查询总金额
        row = cursor.fetchone()
        f1 = open('static/images/in.png', 'wb')
        f1.write(row[0])
        f2 = open('static/images/out.png', 'wb')
        f2.write(row[1])
        f1.close()
        f2.close()
        cursor = connection.cursor()  # 使用自定义sql
        cursor.execute("select * from car_car where plate_number = '%s'" % (plate_number))  # 查询总金额
        row = cursor.fetchone()
        in_date = row[1]
        in_date = in_date.strftime("%Y-%m-%d %H:%M:%S")
        out_date = row[2]
        out_date = out_date.strftime("%Y-%m-%d %H:%M:%S")
        money = row[4]
        in_info = row[6]
        out_info = row[7]
        tojump = 0
        # plate.objects.filter(plate_number=plate_number).delete()
    context = {
        'session_name' : session_name,
        'in_date' : in_date,
        'out_date': out_date,
        'money': money,
        'in_info': in_info,
        'out_info': out_info,
        'plate_number': plate_number,
        'tojump': tojump,
    }
    return render(request, 'operator/index.html', context)


# 操作员 - 首页 - 确认收费
def operator_conCharges(request):
    if request.method == "POST":
        plate = request.POST['plate']
        money = request.POST['money']
        collector = request.POST['collector']
        pay = request.POST['pay']
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # print(plate, money, collector, pay, now)
        chage_money.objects.create(charge_type=pay,total_money=money,charge_time=now)
        charge.objects.create(plate_number=plate, charge_type=pay, charge_time=now,collector=collector)
        return redirect('operator/index.html')


# 操作员 - 黑名单
def operatorBlackList(request):
    session_name = request.session.get('operator')  # 获取管理员的名字
    ret = blacklist.objects.all()
    context = {
        'blacklists': ret,
        'session_name': session_name,
    }
    return render(request, 'operator/blackList.html', context)


# 操作员 - 黑名单 - 新增黑名单
def operator_blacklist_add(request):
    if request.method == "POST":
        plate_number = request.POST['plate_number']
        in_time = request.POST['in_time']
        info = request.POST['info']
        ret = blacklist.objects.create(plate_number=plate_number, black_time=in_time, vlolation_info=info)
        if ret != None:
            return redirect('operator/blackList.html')
        else:
            return render(request, 'operator/blackList.html')


# 操作员 - 当日车辆信息
def operatorCarDay(request):
    session_name = request.session.get('operator')  # 获取管理员的名字
    now = datetime.datetime.now().strftime('%Y-%m-%d')
    ret = car.objects.filter(in_date__date=now).order_by('in_date')
    context = {
        'carDayLists': ret,
        'session_name': session_name,
    }
    return render(request, 'operator/carDay.html', context)


# 操作员 - 车辆历史信息
def operatorCarHistory(request):
    session_name = request.session.get('operator')  # 获取管理员的名字
    ret = car.objects.filter(out_date__isnull=False).order_by('in_date').reverse()
    context = {
        'carHistory': ret,
        'session_name': session_name,
    }
    return render(request, 'operator/carHistory.html', context)


# 操作员 - 实时车辆信息
def operatorCarReal(request):
    session_name = request.session.get('operator')  # 获取管理员的名字
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    utc = arrow.utcnow()  # 获取现在的utc时间
    local = utc.to('local')  # 将utc时间转换为本地时间
    local_zero = local.replace(hour=0, minute=0, second=0)
    today = local_zero.format("YYYY-MM-DD HH:mm:ss")  # 输出当天零点时间
    # print(today)
    ret = car.objects.filter(Q(out_date=None) & Q(in_date__lte=now) & Q(in_date__gt=today)).order_by('in_date')
    context = {
        'realLists': ret,
        'session_name': session_name,
    }
    return render(request, 'operator/carReal.html', context)


# 操作员 - 收费记录
def operatorChargeRecord(request):
    session_name = request.session.get('operator')  # 获取管理员的名字
    ret = charge_money_view.objects.all().order_by('charge_time').reverse()
    context = {
        'session_name': session_name,
        'recordLists': ret,
    }
    return render(request, 'operator/chargeRecord.html', context)


# 操作员 - 密码修改
def operatorPasswordEdit(request):
    session_name = request.session.get('operator')  # 获取管理员的名字
    context = {
        'session_name': session_name,
    }
    return render(request, 'operator/passwordEdit.html', context)


# 操作员 - 修改密码
def operator_editpassword(request):
    if request.method == "POST":
        username = request.POST['this_username']
        password = request.POST['this_password']
        new_password = request.POST['new_password']
        try:
            ret = userinfo.objects.get(username=username, password=password)
            userinfo.objects.filter(username=username, password=password).update(password=new_password)
            return redirect('/login.html')
        except:
            return render(request, 'operator/passwordEdit.html', {"status": "输入的用户名或密码错误"})


# 注销
def logout(request):
    return redirect('/login.html')
