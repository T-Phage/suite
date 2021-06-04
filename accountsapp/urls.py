from django.urls import path
from django.contrib.auth import views as auth_views
from .import views

urlpatterns = [
    path('', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('changepassword/', views.changepassword, name='changepassword'),

    # change password
    path('change_password/', auth_views.PasswordChangeView.as_view(template_name='changepassword.html'),
         name='password_change'),
    path('change_password_done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
         name='password_change_done'),
]