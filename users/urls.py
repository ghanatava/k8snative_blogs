from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns=[
    path('',views.register,name="register"),
    path('login/',auth_views.LoginView.as_view(template_name="users/login.html"),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name="users/logout.html"),name='logout'),
    path('profile/',views.profile,name="profile"),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name="users/password_reset.html"),name='reset_password'),
    path('password_reset/done',auth_views.PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"),name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"),name='password_reset_confirm'),
    path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
]
