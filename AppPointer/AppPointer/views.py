from django.shortcuts import redirect, render

def home(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect("admin_app:home")
        else:
            return redirect("user_app:home")
    else:
        return render(request, 'homepage.html')