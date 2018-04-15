from django.urls import path

from . import views

app_name = 'currentLocation'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:device_id>/', views.detail, name='detail'),
    path('<int:device_id>/vote',views.vote,name='vote')
]