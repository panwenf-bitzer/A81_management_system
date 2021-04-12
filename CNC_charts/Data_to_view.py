import datetime
import sqlite3
from CNC_charts.models import *

class Unplan_downtime():
    def get_unplan_downtime(self,search_date):
        current_time=datetime.datetime.now()
        a=list(list(Unplan_downtime_table.objects.values_list('Mechanic','Electric','Hydraulic','Media','Jig','Waiting','Others').order_by('-cid')[:1])[0])
        b=list(list(Unplan_downtime_table.objects.values_list('Mechanic','Electric','Hydraulic','Media','Jig','Waiting','Others').order_by('-cid')[:1])[0])
        c=list(list(Unplan_downtime_table.objects.values_list('Mechanic','Electric','Hydraulic','Media','Jig','Waiting','Others').order_by('-cid')[:1])[0])
        return [a,b,c]

class Plan_downtime():
    def get_plan_downtime(self,search_date):
        current_time=datetime.datetime.now()
        a=list(list(plan_downtime_table.objects.values_list('Training','Meeting','Optimization','Warm_up','Bipros','Sample','waiting_fixture','Maintenance','program_loading').order_by('-cid')[:1])[0])
        b=list(list(plan_downtime_table.objects.values_list('Training','Meeting','Optimization','Warm_up','Bipros','Sample','waiting_fixture','Maintenance','program_loading').order_by('-cid')[:1])[0])
        c=list(list(plan_downtime_table.objects.values_list('Training','Meeting','Optimization','Warm_up','Bipros','Sample','waiting_fixture','Maintenance','program_loading').order_by('-cid')[:1])[0])
        return [a,b,c]

class OEE_DATA():
    def get_OEE(self,search_date):
        shiftA=list(list(OEE.objects.values_list('A_shift').order_by('-OEE_id')[:1])[0])
        shiftB = list(list(OEE.objects.values_list('B_shift').order_by('-OEE_id')[:1])[0])
        shiftC = list(list(OEE.objects.values_list('C_shift').order_by('-OEE_id')[:1])[0])
        return [shiftA[0],shiftB[0],shiftC[0]]

class Productivity_DATA():
    def get_Productivity(self,search_date):
        current_time=datetime.datetime.now()
        A=list(list(Productivity.objects.values_list('A_shift').order_by('-Pro_id')[:1])[0])
        B = list(list(Productivity.objects.values_list('B_shift').order_by('-Pro_id')[:1])[0])
        C = list(list(Productivity.objects.values_list('C_shift').order_by('-Pro_id')[:1])[0])
        return [A[0],B[0],C[0]]

def get_yestoday():
    today=datetime.date.today()
    oneday=datetime.timedelta(days=1)
    yesterday=today-oneday
    return yesterday


