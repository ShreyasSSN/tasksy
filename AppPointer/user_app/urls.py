from django.urls import path
from . import views

app_name = "user_app"

urlpatterns = [
    path('',views.home, name="home"),
    path('user_profile/',views.user_profile, name="profile"),
    path('user_points/',views.user_points, name="points"),
    path('user_tasks/',views.user_tasks, name="tasks"),
    path('<slug>/',views.app_detail, name="detail"),
]