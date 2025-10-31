from django.shortcuts import render, HttpResponse
from .forms import UserLoginForm, UserRegistrationForm, Profile
from django.contrib import auth
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, template_name='user/login_page.html', context=context)


def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user:login'))
    else:
        form = UserRegistrationForm()
    context = {"form": form}
    return render(request, template_name="user/registration_page.html", context=context)


@login_required
def profile(request):
    if request.method == "POST":
        form = Profile(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("user:profile"))
        else:
            print(form.errors)
    else:
        form = Profile(instance=request.user)
    context = {"form": form}
    return render(request, template_name='user/profile.html', context=context)


@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('user:login'))
