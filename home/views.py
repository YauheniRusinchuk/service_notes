from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth.models import User
from home.forms import UserRegistrateForm
from home.models import Profile
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request, 'home/index.html', {})
    else:
        return render(request, 'home/guest.html', {})


def registration(request):
    form = UserRegistrateForm()
    if request.method == "POST":
        form = UserRegistrateForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            user = User.objects.create_user(username, password=password, email=email)
            profile = Profile.objects.create(user=user)
            #send_mail('WELCOM!', "You registration in service", "Yauheni", [email])
            return redirect('home:login_user')
            #return HttpResponseRedirect(reverse('home:login_user'))
        else:
            form = UserRegistrateForm()
    return render(request, 'home/registration.html', {'form': form})
