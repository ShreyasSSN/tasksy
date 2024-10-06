from django.shortcuts import render, redirect
from admin_app.models import Application
from . import forms
from .models import UserData
from accounts.models import CustomUser

def home(request):
    added_applications = Application.objects.all()
    return render(request, 'user_app/user_home.html', {'app_list':added_applications})

def app_detail(request, slug):
    app = Application.objects.get(app_slug=slug)
    existing_screenshot = UserData.objects.filter(user=request.user, app_name=app.app_name).first()
    if existing_screenshot:
        return render(request, "user_app/app_detail.html", {
            'app':app,
            'screenshot' : existing_screenshot
        })
    if request.method == "POST":
        form = forms.AddScreenShot(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.app_name = app.app_name
            instance.points = app.app_points 
            instance.save()
            custom_user = CustomUser.objects.get(user=request.user)
            custom_user.points += app.app_points
            custom_user.save()
            return redirect("user_app:home")
    else:
        form = forms.AddScreenShot()
    return render(request, "user_app/app_detail.html", {'app':app, 'form':form})

def user_profile(request):
    user = request.user
    user_data = UserData.objects.filter(user=user)
    return render(request, 'user_app/user_profile.html', {'user':user, 'user_data': user_data})

def user_points(request):
    user = request.user
    total_points = 0
    user_data = UserData.objects.filter(user=user)
    for data in user_data:
        total_points += data.points
    return render(request, 'user_app/user_points.html', {'user':user, 'user_data': user_data, 'total_points': total_points})

def user_tasks(request):
    downloaded_apps = UserData.objects.values_list('app_name', flat=True)
    app_list = Application.objects.values_list('app_name', flat=True)
    apps_to_be_downloaded = [app for app in app_list if app not in downloaded_apps]
    apps_list = Application.objects.filter(app_name__in=apps_to_be_downloaded)
    return render(request, 'user_app/user_task.html', {'apps_list': apps_list})
    
