"""hdcarsystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from car import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login),
    path('login.html', views.login),
    path('logout', views.logout),
    path('admin/index.html', views.adminIndex),
    path('admin/blackList.html', views.adminBlackList),
    path('admin/carDay.html', views.adminCarDay),
    path('admin/carHistory.html', views.adminCarHistory),
    path('admin/carReal.html', views.adminCarReal),
    path('admin/carSchool.html', views.adminCarSchool),
    path('admin/chargeMoney.html', views.adminChargeMoney),
    path('admin/chargeRecord.html', views.adminChargeRecord),
    path('admin/chargeStandard.html', views.adminChargeStandard),
    path('admin/log.html', views.adminLog),
    path('admin/passwordEdit.html', views.adminPasswordEdit),
    path('admin/userManage.html', views.adminUserManage),
    path('operator/index.html', views.operatorIndex),
    path('operator/blackList.html', views.operatorBlackList),
    path('operator/carDay.html', views.operatorCarDay),
    path('operator/carHistory.html', views.operatorCarHistory),
    path('operator/carReal.html', views.operatorCarReal),
    path('operator/chargeRecord.html', views.operatorChargeRecord),
    path('operator/passwordEdit.html', views.operatorPasswordEdit),
    path('carschool_add', views.carschool_add),
    path('toBlackList', views.toBlackList),
    path('toTemp', views.toTemp),
    path('blacklist_add', views.blacklist_add),
    path('move_temp', views.move_temp),
    path('toEnable', views.toEnable),
    path('delete_chargestandard', views.delete_chargestandard),
    path('add_chargestandard', views.add_chargestandard),
    path('add_userinfo', views.add_userinfo),
    path('delete_userinfo', views.delete_userinfo),
    path('update_userinfo', views.update_userinfo),
    path('editpassword', views.editpassword),
    path('operator_blacklist_add', views.operator_blacklist_add),
    path('operator_editpassword', views.operator_editpassword),
    path('operator_conCharges', views.operator_conCharges),
]
