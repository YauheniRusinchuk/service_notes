from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from home.models import Profile
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='home:homepage')
def index(request):
    return render(request, 'settings/index.html', {})

@login_required(login_url='home:homepage')
def change(request):
    if request.method == "POST":
        user = request.user
        user.username = request.POST['username']
        user.email = request.POST['email']
        Profile.objects.filter(user=user).update(description=request.POST['description'])
        user.save()
        return redirect('settings:settings')
    return render(request, 'settings/change.html', {})
