from django.shortcuts import render, get_object_or_404
from .models import User

def appHome(request):
    users = User.objects.all()
    return render(request, "website/appHome.html", {"users": users})

def appDescription(request, description_id):
    user = get_object_or_404(User, pk=description_id)  # Fetch user object by ID
    return render(request, "website/appDescription.html", {"user": user})  # Use "user"
