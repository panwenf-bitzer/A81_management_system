from django.urls import path
from . import views
urlpatterns = [
    # admin paths
    path('', views.home , name='home'),
    path('index/', views.index , name='index'),
    path('login/',views.admin_login,name='login'),
    path('change_pw_admin/',views.change_pw_admin,name='change password'),
  
    path('manage_std/',views.manage_std,name='manage_student'),
    path('add_std/',views.add_std,name='add Operator'),
    path('edit_std/<int:id>',views.edit_std,name='edit Operator'),
    path('update_std/<int:id>',views.update_std,name='update Operator'),
    path('delete_std/<int:id>',views.delete_std,name='delete Operator'),
    
    path('manage_faculty/',views.manage_faculty,name='manage_faculty'),
    path('add_faculty/',views.add_faculty,name='add faculty'),
    path('edit_stf/<int:id>',views.edit_stf,name='edit faculty'),
    path('update_stf/<int:id>',views.update_stf,name='update faculty'),
    path('delete_faculty/<int:id>',views.delete_faculty,name='delete faculty'),

    path('manage_sub/',views.manage_sub,name='manage_subject'),
    path('add_sub/',views.add_sub ,name='add subject'),
    path('edit_sub/<int:id>',views.edit_sub,name='edit subject'),
    path('update_sub/<int:id>',views.update_sub,name='update subject'),
    path('delete_sub/<int:id>',views.delete_sub,name='delete subject'),

    path('manage_sem/',views.manage_sem,name='manage_semester'),
    path('add_sem/',views.add_sem ,name='add semester'),
    
    path('manage_att/',views.manage_att,name='manage_att'),
    path('add_att/',views.add_att ,name='add att'),
    path('insert/',views.insert_att_sheet ,name='insert data'),
    path('manage_production_plan/',views.manage_production_plan),
    path('reports/',views.reports),
    path('student_report/',views.student_report),
    path('faculty_report/',views.faculty_report),

    # Operator paths
    path('Operator_index/', views.Operator_index , name='stdindex'),
    path('Operator_login/',views.Operator_login,name='stdlogin'),
    path('Operator_profil/<int:id>',views.Operator_profile,name='Operator profile'),
    path('Operator_change_pw/',views.Operator_change_pw),
    path('s_forgot/',views.s_forgot),
    path('Operator_forgetpass/',views.Operator_forgetpass),
    path('Operator_resetpass/<str:em>',views.Operator_resetpass),
    path('Operator_index/production_plan/',views.Production_plan),
    path('Operator_index/production_plan/add_production_plan/',views.add_Production_plan),
    path('Operator_index/view_att/<int:id>',views.view_att),


    #Operator dashboard

    path('Dashboard/Productivity/', views.ChartView1.as_view(),),
    path('Dashboard/Plan_downtime/', views.ChartView2.as_view(),),
    path('Dashboard/Unplan_downtime', views.ChartView3.as_view(),),
    path('Dashboard/Gauge_shiftA/', views.ChartView4.as_view(),),
    path('Dashboard/Gauge_shiftB/', views.ChartView5.as_view(),),
    path('Dashboard/Gauge_shiftC/', views.ChartView6.as_view(),),


    # engineer paths
    path('Engineer_index/', views.Engineer_index , name='stfindex'),
    path('Engineer_login/',views.Engineer_login,name='stflogin'),
    path('Engineer_profil/<int:id>',views.Engineer_profil,name='Engineer profile'),
    path('Engineer_change_pw/',views.Engineer_change_pw),
    path('Engineer_index/manage_att_std/<int:id>',views.manage_att_std,name='attendance_subject_list'),
    path('Engineer_index/manage_att_std/mark_attendance/<int:id1>/<int:id2>',views.mark_attendance,name='attendance_list'),
    path('make_attendance/<int:semid>/<int:subid>',views.make_attendance,name='marking Operator CNC_charts'),
    path('Engineer_index/my_lecs/<int:id>',views.my_lecs,name='faculty report'),
    path('Engineer_forgot/',views.Engineer_forgot),
    path('Engineer_forgetpass/',views.Engineer_forgetpass),
    path('Engineer_resetpass/<str:em>',views.Engineer_resetpass),
]