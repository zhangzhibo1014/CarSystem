from .models import *

# 在校人员信息视图
class car_school_view(models.Model):
    plate_number = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=10)
    sex = models.CharField(max_length=1)
    word_number = models.CharField(max_length=20)
    idcard = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    partment_name = models.CharField(max_length=20)

    class Meta:
        db_table = 'car_school_view'

# 用户视图
class user_view(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    sex = models.CharField(max_length=1)
    job = models.CharField(max_length=50)
    idcard = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    power_name = models.CharField(max_length=20)

    class Meta:
        db_table = 'user_view'


# 收费金额视图
class charge_money_view(models.Model):
    plate_number = models.CharField(max_length=20, primary_key=True)
    car_type = models.CharField(max_length=20)
    stay_date = models.IntegerField(null=True)
    money = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    charge_type = models.CharField(max_length=20)
    charge_time = models.DateTimeField()
    collector = models.CharField(max_length=20)

    class Meta:
        db_table = 'charge_money_view'

