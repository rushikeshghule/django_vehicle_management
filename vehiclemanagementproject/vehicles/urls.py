from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('create/', views.vehicle_create, name='vehicle_create'),
    path('list/', views.vehicle_list, name='vehicle_list'),
    path('update/<int:pk>/', views.vehicle_update, name='edit_vehicle'),
    path('delete/<int:pk>/', views.vehicle_delete, name='delete_vehicle'),
    path('unauthorized/', views.unauthorized, name='unauthorized'),

]