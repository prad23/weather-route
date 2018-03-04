from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
#    path('<devicename>/', views.device, name='devicename')
]