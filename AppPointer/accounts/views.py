from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import CustomUser

def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            CustomUser.objects.create(user=user, points=0)
            login(request, user)
            return redirect("user_app:home")
    else:
        form = UserCreationForm()
    return render(request, "accounts/signup.html", {'form': form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            redirect_url = request.POST.get('next') or (
                "admin_app:home" if user.is_superuser else "user_app:home"
            )
            return redirect(redirect_url)
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {'form': form})

def logout_view(request):
    if request.method == "POST":
        logout(request)
    return redirect("/")