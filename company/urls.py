from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('update/',views.update,name='update'),
    path('change/',views.change,name='changepass'),
    path('changepass/',views.changepass,name='cpass'),
    path('orders/',views.orders,name='orders'),
    path('policy/',views.policy,name='policy'),
    path('del_upload/',views.upload,name='upload'),
    path('del_new/',views.upload_new,name='up_new'),
]