from django.urls import path
from . import views

app_name = "admin_app"

urlpatterns = [
    path('',views.home, name="home"),
    path('add_app/', views.add_app, name="add_app"),
    path('show_apps/', views.show_all_apps, name="show_apps"),
    path('show_users/', views.show_all_users, name="show_users"),
    path('<slug>/', views.app_detail, name="detail"),
    path('delete_app/<int:id>/', views.app_delete, name="app_delete"),
    path('user/<int:id>/', views.user_data, name="user_data"),
    path('delete_user/<int:id>/', views.delete_user, name="delete_user"),
]