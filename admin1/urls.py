from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name='adminlogin'),
    path('addde/',views.addde,name='addde'),
    path('addcmp/',views.demo,name='addcmp')
]