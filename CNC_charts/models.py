from django.db import models
# Create your models here.

# Admin Table
class Admin(models.Model):
    admin_id = models.AutoField(primary_key='True')
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

# Shift Table
class Shift_table(models.Model):
    shift_id = models.AutoField(primary_key='True')
    shift = models.CharField(max_length=10,unique='True')

#Operator Table
class Operator_Data(models.Model):
    operator_id = models.AutoField(primary_key='True')
    Roll_no = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=100,unique='True')
    email = models.CharField(max_length=100,unique='True')
    password = models.CharField(max_length=100)
    OP_shi = models.ForeignKey(Shift_table,on_delete=models.CASCADE,to_field="shift_id")
    class Meta:
        db_table='Operator_master'
    
# Engineer Table
class Engineer_Data(models.Model):
    f_id = models.AutoField(primary_key='True')
    Roll_no = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,unique='True')
    password = models.CharField(max_length=100)

# Type Table
class Type_Table(models.Model):
    Type_id = models.AutoField(primary_key='True')
    Type_name = models.CharField(max_length=100)

# Attendance Table
# class Attendance_Master(models.Model):
#     att_id = models.AutoField( db_index=True,primary_key=True)
#     shift = models.ForeignKey(Shift_table,on_delete=models.CASCADE)
#     operator = models.ForeignKey(Operator_Data,on_delete=models.CASCADE)
#     type = models.ForeignKey(Type_Table,on_delete=models.CASCADE)
#     leader = models.ForeignKey(Engineer_Data,on_delete=models.CASCADE)
#     class Meta:
#         db_table='Attendance_master'
#         unique_together = (('shift', 'operator','type','leader'),)

class Attendance_Master(models.Model):
    # att_id=models.AutoField(primary_key=True)
    Roll_no= models.IntegerField(unique=True)
    Shift=models.ForeignKey(Shift_table,on_delete=models.CASCADE)
    Name=models.CharField(max_length=10,unique=True)
    Roll_in = models.DateTimeField(unique_for_date=True)
    Roll_out=models.DateTimeField()
    Attendace_time = models.FloatField(max_length=10)
    class Meta:
        db_table='Attendance_master'
        # unique_together = ('Name', 'Roll_in','Roll_out','Attendace_time','Shift')

# operator CNC_charts Table
class Operator_Attendance_Sheet(models.Model):
        operator_att_id = models.AutoField(primary_key='True')
        date = models.DateField(auto_now_add='True')
        att = models.ForeignKey(Attendance_Master , on_delete=models.CASCADE)
        present = models.CharField(max_length=3)

# CNC ID
class CNC_ID(models.Model):
    Cid=models.AutoField(primary_key=True)
    Cnc_name=models.CharField(max_length=10)
# Plan_downtime Table

class plan_downtime_table(models.Model):
    cid = models.AutoField(primary_key=True)
    Date = models.DateField(unique_for_date=True)
    shift=models.ForeignKey(Shift_table , on_delete=models.CASCADE)
    Operator = models.ForeignKey(Operator_Data , on_delete=models.CASCADE)
    Cnc = models.ForeignKey(CNC_ID, on_delete=models.CASCADE)
    Training = models.IntegerField()
    Meeting = models.IntegerField()
    Optimization=models.IntegerField()
    Warm_up = models.IntegerField()
    Bipros = models.IntegerField()
    Sample = models.IntegerField()
    waiting_fixture = models.IntegerField()
    Maintenance = models.IntegerField()
    program_loading = models.IntegerField()

# UnPlan_downtime Table
class Unplan_downtime_table(models.Model):
    cid = models.AutoField(primary_key=True)
    Date = models.DateField(unique_for_date=True)
    shift = models.ForeignKey(Shift_table, on_delete=models.CASCADE)
    Operator = models.ForeignKey(Operator_Data, on_delete=models.CASCADE)
    Cnc = models.ForeignKey(CNC_ID, on_delete=models.CASCADE)
    Mechanic = models.IntegerField()
    Electric = models.IntegerField()
    Hydraulic=models.IntegerField()
    Media = models.IntegerField()
    Jig = models.IntegerField()
    Waiting = models.IntegerField()
    Others = models.IntegerField()
# MAchine OEE shifts
class OEE(models.Model):
    OEE_id= models.AutoField(primary_key=True)
    Date = models.DateField(unique_for_date=True)
    A_shift=models.FloatField(max_length=10)
    B_shift=models.FloatField(max_length=10)
    C_shift=models.FloatField(max_length=10)
# Machine_productivity
class Productivity(models.Model):
    Pro_id= models.AutoField(primary_key=True)
    Date = models.DateField(unique_for_date=True)
    A_shift=models.FloatField(max_length=10)
    B_shift=models.FloatField(max_length=10)
    C_shift=models.FloatField(max_length=10)
