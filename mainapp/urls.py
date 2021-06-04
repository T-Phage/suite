from django.urls import path
from .import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('repoadd_site_memberssitory/', views.repository, name='repository'),
    path('mysite/', views.mysite, name='mysite'),
    path('faculty/<str:pk>/', views.faculty, name='faculty'),
    path('department/<str:pk>/', views.department, name='department'),
    path('open_site/<str:pk>/', views.open_site, name='open_site'),
    path('folder/<str:pk>/', views.folder, name='folder'),
    path('save_folder/', views.savefolder, name='savefolder'),
    path('save_file/', views.save_file, name='save_file'),
    path('read/<str:pk>/', views.docview, name='docview'),
    path('add_site_members/<str:pk>/', views.add_site_members, name='add_site_members'),
    path('add_site_member_ajax/', views.add_site_member_ajax, name='add_site_member_ajax'),
    path('save_siteform/', views.save_siteform, name='save_siteform'),
]