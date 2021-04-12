from django.shortcuts import render , redirect
# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth import authenticate , login , logout
from django.contrib.sessions.models import Session
from django.db import connection
from CNC_charts.models import *
from CNC_charts.forms  import *
from .resources import AttendanceResources , OperatorResources
from tablib import Dataset
from django.core import serializers
from django.core.mail import send_mail

import json,datetime
from django.http import HttpResponse
from rest_framework.views import APIView

from pyecharts.charts import Line,Bar,Pie,Gauge,Grid
from pyecharts import options as opts
from. import Data_to_view,fetch_data
# Create your views here.

### ADMIN TASK IS DONE HERE.....................................................................

def home(request):
    return render(request,'home.html')
   
def admin_login(request): 
    context={}
    count = 0
    if request.method == "POST":
        eusername = request.POST['username']
        epassword = request.POST['password']
        count=Admin.objects.filter(username=eusername,password=epassword).count()
        if  count>0:
            request.session['is_logged'] = eusername
            return redirect('/index/')
        else:
            context['error']= 'Enter valid username or password...'
            return render(request,'login.html',context)
    return render(request,'login.html') 

def index(request):
            if (request.session.has_key('is_logged')):
                 return render(request,'index.html')
            return redirect('/login/')


def change_pw_admin(request):
    context={}
    count = 0
    if request.method == "POST":
        eusername = request.POST['username']
        epassword = request.POST['password']
        ecpassword = request.POST['cpassword']
        count=Admin.objects.filter(username=eusername,password=epassword).count()
        if  count>0:
            Admin.objects.filter(username=eusername,password=epassword).update(password=ecpassword)
            return redirect('/login/')
        else:
            context['error']= 'Enter valid username or password...'
            return render(request,'change_pw.html',context)
    return render(request,'change_pw.html')


### Operator CRUD IS PERFORMS HERE...................................................

def manage_std(request):   #READ Operator DATA
        form = Operator_Data.objects.all()
        return render(request ,'Engineer/manage_Operator.html',{'form':form})


def add_std(request):     #INSERT STUDENT DATA
        form = OperatorForm()
        if request.method == 'POST':
            form = OperatorForm(request.POST)
            if form.is_valid:
                form.save()
                return redirect('/manage_std/')
            else:
                return render(request,'Engineer/add_Operator.html',{'form':form})
        else:
            return render(request,'Engineer/add_Operator.html',{'form':form})


def edit_std(request,id): #EDIT TABLE
    student = Operator_Data.objects.get(operator_id=id)
    return render(request,'Engineer/editstd.html', {'form':student})
    

def update_std(request,id):  # UPDATE STUDENT DATA 
   student = Operator_Data.objects.get(operator_id=id)
   form = OperatorForm(request.POST , instance=student)
   if form.is_valid(): 
           form.save()
           return redirect("/manage_std/")
   return render(request,'Engineer/editstd.html',{'form':student})

def delete_std(request,id):  # DELETE STUDENT DATA
    student = Operator_Data.objects.get(operator_id=id)
    student.delete()  
    return redirect("/manage_std")  

### FACULTY CRUD PERFORMS HERE...

def manage_faculty(request):
        form = Engineer_Data.objects.all()
        return render(request ,'Engineer/manage_Engineer.html',{'form':form})

def add_faculty(request):
        form = EngineerForm
        if request.method == 'POST':
            form = EngineerForm(request.POST)
            if form.is_valid:
                form.save()
                return redirect('/manage_faculty')
            else:
                return render(request,'Engineer/add_Engineer.html',{'form':form})
        else:
            return render(request,'Engineer/add_Engineer.html',{'form':form})
def edit_stf(request,id): #EDIT TABLE
    faculty = Engineer_Data.objects.get(f_id=id)
    return render(request,'Engineer/editstf.html', {'form':faculty})
    

def update_stf(request,id):  # UPDATE STUDENT DATA 
   faculty = Engineer_Data.objects.get(f_id=id)
   form = EngineerForm(request.POST , instance=faculty)
   if form.is_valid(): 
           form.save()
           return redirect("/manage_faculty/")
   return render(request,'Engineer/editstf.html',{'form':faculty})

def delete_faculty(request,id): 
    faculty = Engineer_Data.objects.get(f_id=id)
    faculty.delete()  
    return redirect("/manage_faculty") 


# operator CRUD.....
def manage_sub(request):
        form = Type_Table.objects.all()
        return render(request ,'Engineer/manage_sub.html',{'form':form})

def add_sub(request):
        form = TypeForm
        if request.method == 'POST':
            form = TypeForm(request.POST)
            if form.is_valid:
                form.save()
                return redirect('/manage_sub')
            else:
                return render(request,'Engineer/add_Type.html',{'form':form})
        else:
            return render(request,'Engineer/add_Type.html',{'form':form})

def edit_sub(request,id): #EDIT TABLE
    subject = Type_Table.objects.get(Type_id=id)
    return render(request,'Engineer/editsub.html', {'form':subject})

def update_sub(request,id):  # UPDATE STUDENT DATA 
    subject = Type_Table.objects.get(Type_id=id)
    form = TypeForm(request.POST , instance=subject)
    if form.is_valid(): 
        form.save()
        return redirect("/manage_sub/")
    return render(request,'Engineer/editsub.html',{'form':subject})

def delete_sub(request,id): 
    subject = Type_Table.objects.get(Type_id=id)
    subject.delete()  
    return redirect("/manage_sub/") 



# shift CRUD.....
def manage_sem(request):
        form = Shift_table.objects.all()
        return render(request ,'Engineer/manage_Shift.html',{'form':form})

def add_sem(request):
        form = ShiftForm
        if request.method == 'POST':
            form = ShiftForm(request.POST)
            if form.is_valid:
                form.save()
                return redirect('/manage_sem/')
            else:
                return render(request,'Engineer/add_Shift.html',{'form':form})
        else:
            return render(request,'Engineer/add_Shift.html',{'form':form})


#production CRUD
def add_Production_plan(request):
    if (request.session.has_key('is_std_logged')):
        #context={}
        form = PlanDowntimeForm()
        if request.method == 'POST':
            form = PlanDowntimeForm(request.POST)
            if form.is_valid():
                     form.save()
                     #context={'success':"your production_plan has been sent..."}
                     #return render(request,'Operator/add_production_plan.html',context)
                     return redirect('/Engineer_index/')
            else:
                return render(request,'Engineer/add_production_plan.html',{'form':form})
        else:
            return render(request,'Engineer/add_production_plan.html',{'form':form})
    return redirect('/Engineer_login/')


# CNC_charts operations....
def manage_att(request):
       form = Attendance_Master.objects.all().order_by('id')
       return render(request ,'Engineer/manage_att.html',{'form':form})
    

def add_att(request):
            return render(request,'Engineer/add_att.html')

def insert_att_sheet(request):
    context={}
    if request.method == 'POST':
        att_resource = AttendanceResources()
        dataset = Dataset()
        dataset.headers=['Roll_no','Shift','Name', 'Roll_in','Roll_out','Attendace_time']
        new_sheet = request.FILES['mysheet']

        if not new_sheet.name.endswith('xlsx'):
            context['message']="File must be in excel formate only..."
            return render(request,'Engineer/add_att.html',context)
        import_data = dataset.load(new_sheet.read(),format='xlsx')

        for data in import_data:
           #   value = Attendance_Master(
           #       data[0],
           #       data[1],
           #       data[2],
           #       data[3],
           #       data[4],
           #       data[5],
           # )
           #   value.save()
            # print(data[0], data[1], data[2], data[3], data[4], data[5])
            Attendance_Master.objects.update_or_create(Roll_no= data[0],Shift=Shift_table(shift_id=3), Name=data[2], Roll_in=data[3],Roll_out=data[4],Attendace_time=data[5])

        return redirect('/manage_att/')
        
def manage_production_plan(request):
    form = plan_downtime_table.objects.all()
    return render(request,'Engineer/manage_production_plam.html',{'form':form})




# OPERATIONS OF Operator MODULES...

def Operator_index(request):
       if (request.session.has_key('is_std_logged')):
            data = request.session['is_std_logged']
            s = Operator_Data.objects.get(email=data)
            return render(request,'Operator/index.html',{'form':s})
       return redirect('/Operator_login/')

def Operator_login(request):
    context={}
    count = 0
    if request.method == "POST":
        eusername = request.POST['email']
        epassword = request.POST['password']
        count=Operator_Data.objects.filter(email=eusername,password=epassword).count()
        if  count>0:
            request.session['is_std_logged'] = eusername
            return redirect('/Operator_index/')
        else:
           context['error']= 'Enter valid username or password...'
           return render(request,'Operator/login.html',context)
    return render(request,'Operator/login.html')

def Operator_profile(request,id):
    if (request.session.has_key('is_std_logged')):
            data = request.session['is_std_logged']
            s = Operator_Data.objects.get(email=data)
            return render(request,'Operator/Operator_profile.html',{'form':s})
    return redirect('/std_login/')

def Operator_change_pw(request):
    context={}
    count = 0
    if request.method == "POST":
        eusername = request.POST['username']
        epassword = request.POST['password']
        ecpassword = request.POST['cpassword']
        count=Operator_Data.objects.filter(email=eusername,password=epassword).count()
        if  count>0:
            Operator_Data.objects.filter(email=eusername,password=epassword).update(password=ecpassword)
            return redirect('/Operator_login/')
        else:
            context['error']= 'Enter valid username or password...'
            return render(request,'Operator/change_pw.html',context)
    return render(request,'Operator/change_pw.html')

def Production_plan(request):
    if (request.session.has_key('is_std_logged')):
        return render(request,'Operator/production_plan.html')
    return redirect('/Operator_login/')

def view_att(request,id):
    if request.session.has_key('is_std_logged'):
        cursor = connection.cursor()
        cursor.callproc('studentAttendance',[id])
        res = cursor.fetchall()
        result = []
        for r in res:
            result.append(r)
            #result.sort()
            #print(result)
        return render(request,'Operator/view_attendance.html',{'data':result})
    return render(request,'Operator/login.html')

def s_forgot(request):
        return render(request,'Operator/forgot_password.html')

def Operator_forgetpass(request):
    count =0 
    if request.method == 'POST':
        em = request.POST['email']
        print(type(em))
        count = Operator_Data.objects.filter(email=em).count()
        if count > 0:
            title = 'Attendance Management System Password Reset'
            link = 'http://127.0.0.1:8000/std_resetpass/'+ em
            send_mail(title,'Here we send you a link to reset your password :\n' + link ,'soninisha2709@gmail.com',[em],fail_silently=False)
            msg = 'Your request has been sent please check your mail....'
            return render(request,'Operator/forgot_password.html',{'success':msg})
        msg = 'Please enter your registered Email ID...'
        return render(request,'Operator/forgot_password.html',{'fail':msg})
    return render(request,'Operator/forgot_password.html')

def Operator_resetpass(request,em):
    context={}
    count =0
    count =  Operator_Data.objects.filter(email=em).count()
    if count>0:
            if request.method == "POST":
                psw = request.POST['password']
                cpass= request.POST['cpassword']
                if psw == cpass:
                    Operator_Data.objects.filter(email=em).update(password=psw)
                    return redirect('/std_index/')
                else:
                    context={'error':'Password and Confirm password should not match...'}
                    return render(request,'Operator/reset_password.html',context)
    return render(request,'Operator/reset_password.html',{'email':em})




## OPERATIONS OF Manager MODULES...

def Engineer_index(request):
    if (request.session.has_key('is_flt_logged')):
            data = request.session['is_flt_logged']
            f = Engineer_Data.objects.get(email=data)
            return render(request,'Engineer/index.html',{'form':f})
    return redirect('/stf_login/')

def Engineer_login(request):
    context={}
    count = 0
    if request.method == "POST":
        eusername = request.POST['email']
        epassword = request.POST['password']
        count=Engineer_Data.objects.filter(email=eusername,password=epassword).count()
        if  count>0:
            request.session['is_flt_logged'] = eusername
            return redirect('/Engineer_index/')
        else:
           context['error']= 'Enter valid username or password...'
           return render(request,'Engineer/login.html',context)
    return render(request,'Engineer/login.html')

def Engineer_profil(request,id):
    f = Engineer_Data.objects.get(f_id=id)
    return render(request,'Engineer/Engineer_profil.html',{'form':f})

def Engineer_change_pw(request):
    context={}
    count = 0
    if request.method == "POST":
        eusername = request.POST['username']
        epassword = request.POST['password']
        ecpassword = request.POST['cpassword']
        count=Engineer_Data.objects.filter(email=eusername,password=epassword).count()
        if  count>0:
            Engineer_Data.objects.filter(email=eusername,password=epassword).update(password=ecpassword)
            return redirect('/Engineer_login/')
        else:
            context['error']= 'Enter valid username or password...'
            return render(request,'Engineer/change_pw.html',context)
    return render(request,'Engineer/change_pw.html')


def manage_att_std(request,id):
    if request.session.has_key('is_flt_logged'):
             sub = Type_Table.objects.filter(faculty=id)
             return render(request,'Engineer/attendancesheet.html',{'form':sub})
    return render(request,'Engineer/login.html')

def mark_attendance(request,id1,id2):
    if request.session.has_key('is_flt_logged'):
        cursor = connection.cursor()
        cursor.callproc('attendaceProcedure',[id1,id2])
        res = cursor.fetchall()
        result = []
        for r in res:
            result.append(r)
            result.sort()
            #print(result)
        return render(request,'Engineer/make_att.html',{'data':result})
    return render(request,'Engineer/login.html')

    
def make_attendance(request,semid,subid): 
    std_attid=[] 
    count = 0
    if request.session.has_key('is_flt_logged'):
        if request.method == 'POST':
            att_id = request.POST['att']
            print(att_id)
            a = Attendance_Master.objects.filter(sem = semid , sub =subid).order_by('att_id')
            for aid in a:
                std_attid.append(aid.att_id)
            print('Operator att id=',std_attid)
            present = att_id.split(",")
            present_attid = []
            for i in range(len(present)-1): 
                present_attid.append(int(present[i]))
            print('Present att id=',present_attid)
            for x in std_attid:
                count = 0
                for y in present_attid:
                    if x == y:
                         attendance = Operator_Attendance_Sheet(att=x,present=1)
                         attendance.save()
                         count = 1
                if count == 0:
                        attendance = Operator_Attendance_Sheet(att=x,present=0)
                        attendance.save()
            return redirect('/stf_index/')
            #return render(request,'Engineer/make_att.html')
    return render(request,'Engineer/login.html')

def my_lecs(request,id):
    if request.session.has_key('is_flt_logged'):
        data = request.session['is_flt_logged']
        fname = Engineer_Data.objects.get(email=data)
        faculty_report = []
        f_report = []
        sub = Type_Table.objects.filter(faculty=id)
        for s in sub:
            print(s.sub_id,"---",s.sub_name)
            aid = Attendance_Master.objects.filter(sub=s.sub_id)
            for a in aid:
                print(a.att_id)
                lec = Operator_Attendance_Sheet.objects.filter(att=a.att_id).values('date').count()
                faculty_report=[s.sub_name,lec]
            f_report.append(faculty_report)
        print(f_report)
        f = fname.name
        print(fname.name)
        #print(f)
        return render(request,'Engineer/report.html',{'data':f_report,'name':f})
    return redirect('/stf_index/')

def Engineer_forgot(request):
        return render(request,'Engineer/forgot_password.html')

def Engineer_forgetpass(request):
    count =0 
    if request.method == 'POST':
        em = request.POST['email']
        print(type(em))
        count = Engineer_Data.objects.filter(email=em).count()
        if count > 0:
            title = 'Attendance Management System Reset Password'
            link = 'http://127.0.0.1:8000/stf_resetpass/'+ em
            send_mail(title,'Here we send you a link to reset your password :\n' + link ,'soninisha2709@gmail.com',[em],fail_silently=False)
            msg = 'Your request has been sent please check your mail....'
            return render(request,'Engineer/forgot_password.html',{'success':msg})
        msg = 'Please enter your registered Email ID...'
        return render(request,'Engineer/forgot_password.html',{'fail':msg})
    return render(request,'Engineer/forgot_password.html')

def Engineer_resetpass(request,em):
    context={}
    count =0
    count =  Engineer_Data.objects.filter(email=em).count()
    if count>0:
            if request.method == "POST":
                psw = request.POST['password']
                cpass= request.POST['cpassword']
                if psw == cpass:
                    Engineer_Data.objects.filter(email=em).update(password=psw)
                    return redirect('/std_index/')
                else:
                    context={'error':'Password and Confirm password should not match...'}
                    return render(request,'Engineer/reset_password.html',context)
    return render(request,'Engineer/reset_password.html',{'email':em})
    



# REPORTS ---------------------------------------------------------------------------
def reports(request):
    return render(request,'reports.html')

def student_report(requst):
    context = {}
    std = []
    std_report = []
    count = 0 
    if requst.method == 'POST':
        sem = requst.POST['sem']
        sub = requst.POST['sub']
        student = Operator_Data.objects.filter(s_sem=sem)
        for s in student:
                aid = Attendance_Master.objects.filter(std = s.operator_id,sub=sub)
                for a in aid:
                         count = Operator_Attendance_Sheet.objects.filter(att=a.att_id,present=1).count()
                         std = [s.Roll_no,s.name,count]
                         print(std)
                         std_report.append(std)
        print(std_report)
        context = {'data':std_report}
        return render(requst,'view_reports.html',context)
    return redirect('/reports/')

def faculty_report(request):
    faculty_report = []
    f_report = []
    if request.method == 'POST':
        fclid = request.POST['fid'] 
       # cursor = connection.cursor()
        #cursor.callproc('facultyProgress',[f_id,s_id])
        #res = cursor.fetchall()
        #result = []
        #for r in res:
         #   result.append(r)
          #  result.sort()
           # print(result)
        fname = Engineer_Data.objects.get(f_id= fclid)
        sub = Type_Table.objects.filter(faculty=fclid)
        for s in sub:
            print(s.sub_id,"---",s.sub_name)
            aid = Attendance_Master.objects.filter(sub=s.sub_id)
            for a in aid:
                print(a.att_id)
                lec = Operator_Attendance_Sheet.objects.filter(att=a.att_id).values('date').count()
                faculty_report=[s.sub_name,lec]
            f_report.append(faculty_report)
        print(f_report)
        f = fname.name
        print(fname.name)
        return render(request,'faculty_report.html',{'data':f_report,'name':f})  
    return redirect('/reports/')

#this para is for dashboard
def response_as_json(data):
    json_str = json.dumps(data)
    response = HttpResponse(
        json_str,
        content_type="application/json",
    )
    response["Access-Control-Allow-Origin"] = "*"
    return response


def json_response(data, code=200):
    data = {
        "code": code,
        "msg": "success",
        "data": data,
    }
    return response_as_json(data)


def json_error(error_string="error", code=500, **kwargs):
    data = {
        "code": code,
        "msg": error_string,
        "data": {}
    }
    data.update(kwargs)
    return response_as_json(data)

JsonResponse = json_response
JsonError = json_error

def bar_productivity()-> Bar:
    Y_value=fetch_data.productivity_from_input()
    Y_value=[Y_value[0]*100,Y_value[1]*100,Y_value[2]*100]
    print(Y_value)
    X_data_shift=['Shift_A','Shift_B','Shift_C',]
    target_value=[80,80,80]
    a=(
        Line()
            .add_xaxis(X_data_shift)
            .add_yaxis('target_productivity', target_value)
            .set_global_opts(title_opts=opts.TitleOpts(title="Productivity"))
            .set_global_opts(legend_opts=opts.LegendOpts(pos_left="100"))
            .set_series_opts(label_opts=opts.LabelOpts(position="inside"))
            .set_global_opts(
            yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(formatter="{value} %"), interval=20))


    )
    b=(
        Bar()
        .add_xaxis(X_data_shift)
        .add_yaxis('Productivity', Y_value,label_opts=opts.LabelOpts(formatter="{c} %"))
        .set_global_opts(title_opts=opts.TitleOpts(title="Productivity"))
        .set_global_opts(legend_opts=opts.LegendOpts(pos_left="0"))
        .set_series_opts(label_opts=opts.LabelOpts(position="inside"))
        .set_global_opts(yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(formatter="{value} %"), interval = 20))
        .overlap(a)
        .dump_options_with_quotes()

    )
    return b

def bar_unplandowntime()-> Bar:
    Y_value=Data_to_view.Unplan_downtime().get_unplan_downtime(datetime.datetime.now().date())
    X_data_downtime=['Mechanic','Electric','Hydraulic','Media_missing','Jig_issue','waiting_machine','Others']
    target_value = [20, 20, 20, 20, 20, 10, 10, 10, 15]
    a = (
        Line()
            .add_xaxis(X_data_downtime)
            .add_yaxis('target_downtime', target_value)
            .set_global_opts(title_opts=opts.TitleOpts(subtitle="target"))
            .set_global_opts(legend_opts=opts.LegendOpts(pos_left="100"))
            .set_series_opts(label_opts=opts.LabelOpts(position="inside"))
            .set_global_opts(
            yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(formatter="{value} %"), interval=20)))
    b=(
        Bar()
        .add_xaxis(X_data_downtime)
        .add_yaxis('Shift_A', Y_value[0] )
        .add_yaxis('Shift_B', Y_value[1])
        .add_yaxis('Shift_C', Y_value[2])
        .set_global_opts(title_opts=opts.TitleOpts(title='非计划停机'))
        .set_global_opts(legend_opts=opts.LegendOpts(pos_left="0"),xaxis_opts=opts.AxisOpts(axislabel_opts={"interval":"0"}))
        .set_series_opts(label_opts=opts.LabelOpts(position="inside"))
        .overlap(a)
        .dump_options_with_quotes()
    )
    return b

def bar_plandowntime()-> Bar:
    Y_value=Data_to_view.Plan_downtime().get_plan_downtime(datetime.datetime.now().date())
    X_data_downtime=['Training','meeting','Optimization','Warm_up','Bpros','sample_buiding','waiting','Maintenance','program_download']
    target_value=[20,20,20,20,20,30,40,10,30]
    a = (
        Line()
            .add_xaxis(X_data_downtime)
            .add_yaxis('target_downtime', target_value)
            .set_global_opts(legend_opts=opts.LegendOpts(pos_left="100"),xaxis_opts=opts.AxisOpts(axislabel_opts={"interval":"0"}))
            .set_series_opts(label_opts=opts.LabelOpts(position="inside"))
            .set_global_opts(
            yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(formatter="{value} %"), interval=20)))
    b=(
        Bar()
        .add_xaxis(X_data_downtime)
        .add_yaxis('Shift_A', Y_value[0])
        .add_yaxis('Shift_B', Y_value[1])
        .add_yaxis('Shift_C', Y_value[2])
        .set_global_opts(title_opts=opts.TitleOpts(title='Minutes'))
        .set_global_opts(legend_opts=opts.LegendOpts(pos_left="0"))
        .set_series_opts(label_opts=opts.LabelOpts(position="inside",font_size=6))
        .overlap(a)
        .dump_options_with_quotes())
    return b
def Gauge_shiftA()-> Gauge:
    Data_value= fetch_data.OEE_from_input()
    Data_show='{:0.2f}'.format(Data_value[0]*100)
    b=(
        Gauge()
        .add("OEE_shiftA",[{"",Data_show}],axisline_opts = opts.AxisLineOpts(linestyle_opts= opts.LineStyleOpts(
          color =[(0.5, "red"), (0.8, "yellow"), (1, "green")], width = 20)))
          .set_global_opts(
        tooltip_opts=opts.TooltipOpts(is_show=True, formatter="{a} <br/>{b} : {c}%"),)
        .dump_options_with_quotes()
    )
    return b
def Gauge_shiftB()-> Gauge:
    Data_value= fetch_data.OEE_from_input()
    Data_show='{:0.2f}'.format(Data_value[1]*100)
    b=(
        Gauge()
        .add("OEE_shiftB",[{"",Data_show},],
             axisline_opts=opts.AxisLineOpts(linestyle_opts=opts.LineStyleOpts(
                 color=[(0.5, "red"), (0.8, "yellow"), (1, "green")], width=20)),)
        .set_global_opts(title_opts=opts.TitleOpts(title="OEE_shiftB"))
        .set_global_opts(
            tooltip_opts=opts.TooltipOpts(is_show=True, formatter="{a} <br/>{b} : {c}%"),
        )
        .dump_options_with_quotes()
    )
    return b
def Gauge_shiftC()-> Gauge:
    Data_value= fetch_data.OEE_from_input()
    Data_show='{:0.2f}'.format(Data_value[2]*100)
    b=(
        Gauge()
        .add("OEE_shiftC",[{"",Data_show}],axisline_opts = opts.AxisLineOpts(linestyle_opts= opts.LineStyleOpts(
          color =[(0.5, "red"), (0.8, "yellow"), (1, "green")], width = 20)))
        .set_global_opts(title_opts=opts.TitleOpts(title="OEE_shiftC"))
        .set_global_opts(
            tooltip_opts=opts.TooltipOpts(is_show=True, formatter="{a} <br/>{b} : {c}%"),
        )
        .dump_options_with_quotes()
    )
    return b
class ChartView1(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(bar_productivity()))

class ChartView2(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(bar_plandowntime()))

class ChartView3(APIView):
    def get(self, request, *args, **kwargs):
         return JsonResponse(json.loads(bar_unplandowntime()))

class ChartView4(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(Gauge_shiftA()))

class ChartView5(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(Gauge_shiftB()))

class ChartView6(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(Gauge_shiftC()))
