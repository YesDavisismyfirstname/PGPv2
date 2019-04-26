from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.urls import reverse
from django.shortcuts import render, redirect
from apps.game_window.models import Player 

User = get_user_model()

@login_required(login_url='/log_in/')
def user_list(request):
    """
    NOTE: This is fine for demonstration purposes, but this should be
    refactored before we deploy this app to production.
    Imagine how 100,000 users logging in and out of our app would affect
    the performance of this code!
    """
    users = User.objects.select_related('logged_in_user')
    for user in users:
        user.status = 'Online' if hasattr(user, 'logged_in_user') else 'Offline'
    return render(request, 'login/user_list.html', {'users': users})

def landing(request):
    return render(request, 'login/landing.html')

def log_in(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            logMeIn = form.get_user()
            loginuser = Player.objects.get(user=logMeIn)
            loginuser.logged_in = True
            loginuser.save()
            login(request, form.get_user())
            return redirect("/gamelobby/")
        else:
            print(form.errors)
    return render(request, 'login/login.html', {'form': form})

@login_required(login_url='/log_in/')
def log_out(request):
    loginuser = Player.objects.get(user=request.user)
    loginuser.logged_in = False
    loginuser.save()
    logout(request)
    return redirect(reverse('login:login'))

def sign_up(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            createPlayer = Player.objects.create()
            createPlayer.user = User.objects.last()
            createPlayer.save()
            print(createPlayer)
            return redirect(reverse('login:login'))
        else:
            print(form.errors)
    return render(request, 'login/register.html', {'form': form})
