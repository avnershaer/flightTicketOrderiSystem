from django.urls import path
from . import views

app_name ='plghts_order_system'
urlpatterns = [
        path('', views.index, name='index'),
        path('userRole/', views.userRole, name='userRole')

]