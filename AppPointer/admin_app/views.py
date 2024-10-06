from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from . import app_add
from django.http import HttpResponseRedirect
from .models import Application
from accounts.models import CustomUser
from functools import wraps
from user_app.models import UserData

def admin_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not (request.user.is_superuser):
            messages.error(request, "You are not authorized to access this page")
            return redirect('user_app:home')
        return view_func(request, *args, **kwargs)
    return _wrapped_view



@admin_required
def home(request):
    return render(request, 'admin_app/admin_home.html')

@admin_required
def add_app(request):
    if request.method == "POST":
        form = app_add.AddApplication(request.POST)
        if form.is_valid():
            form.save()
            return redirect("admin_app:home")
    else:
        form = app_add.AddApplication()
    return render(request, 'admin_app/add_app.html', {'form': form})

@admin_required
def show_all_apps(request):
    apps_list = Application.objects.all()
    return render(request, 'admin_app/show_apps.html', {'app_list': apps_list})

@admin_required
def show_all_users(request):
    if not request.user.is_superuser:
        return redirect("user_app:home")
    users = User.objects.all()
    return render(request, 'admin_app/show_users.html', {'users': users})

@admin_required
def app_detail(request, slug):
    app = get_object_or_404(Application, app_slug=slug)
    return render(request, "admin_app/app_detail.html", {'app':app})

@admin_required
def app_delete(request, id):
    app = get_object_or_404(Application, id=id)
    app.delete()
    return redirect("admin_app:show_apps")

@admin_required
def delete_user(request, id):
    user = get_object_or_404(User, id=id)
    try:
        custom_user = CustomUser.objects.get(user=user)  
        custom_user.delete()
    except CustomUser.DoesNotExist:
        pass
    user_data_list = UserData.objects.filter(user=user)
    for user_data in user_data_list:
        user.delete()
    user.delete()
    return redirect("admin_app:show_users")

@admin_required
def user_data(request, id):
    viewed_user = get_object_or_404(User, id=id)
    try:
        custom_user = CustomUser.objects.get(user=viewed_user)  # Fetch the related CustomUser instance
        points = custom_user.points  # Get the points from CustomUser
    except CustomUser.DoesNotExist:
        points = None  # Handle if there's no CustomUser instance
    user_data_list = UserData.objects.filter(user=viewed_user)
    return render(request, 'admin_app/user_detail.html', {'user': viewed_user, 'points': points, 'user_data_list': user_data_list})
