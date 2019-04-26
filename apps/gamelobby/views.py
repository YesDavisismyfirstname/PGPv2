from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.shortcuts import render, redirect
from apps.game_window.models import Lobbies, Player
from apps.gamelobby.forms import newLobby
import json

User = get_user_model()
# Create your views here.

@login_required(login_url='/log_in/')
def gamelobby(request):
    return render(request, 'gamelobby/gamemode.html')

@login_required(login_url='/log_in/')
def pvp(request, room_name =""):
    try:
        currentroom = Lobbies.objects.get(id=room_name)
    except:
        currentroom = ""
    ctx = {
        'rooms' : Lobbies.objects.all(),
        'activeroom': currentroom,
        'room_name_json': mark_safe(json.dumps(room_name)),
        }
    return render(request, 'gamelobby/pvp.html', ctx)

@login_required(login_url='/log_in/')
def pvpNew(request):
    if request.method=="POST":
        newlob = newLobby(request.POST)
        if newlob.is_valid():
            newlob.created_by = request.user
            newlob.save()
            newest = Lobbies.objects.last()
            newest.player.add(request.user.logged_in_user)
            return redirect('/gamelobby/pending/'+str(newest.id))
        else: 
            ctx = {
                'lobby' : newlob
            }
            return render(request, 'gamelobby/pvpnew.html',ctx)
    else:
        lobby = newLobby(initial={'created_by': request.user})
        ctx = {
            'lobby' : lobby
            }
        return render(request, 'gamelobby/pvpnew.html', ctx)

@login_required
def joingame(request,room_name):
    print("HERE")
    currentroom = Lobbies.objects.get(id=room_name)
    print(currentroom)
    currentroom.player.add(request.user.logged_in_user)
    return redirect('/gamelobby/pending/' + str(room_name))

@login_required
def activegame(request,room_name):
    currentroom = Lobbies.objects.get(id=room_name)
    ctx = {
        'activeroom': currentroom,
        'room_name_json': mark_safe(json.dumps(room_name)),
        }
    return render(request, 'gamelobby/activegame.html', ctx)

@login_required
def delRoom(request,room_name):
    #if request.method == "POST":
        currentroom = Lobbies.objects.get(id=room_name)
        currentroom.delete()
        return redirect('/gamelobby/pvp')
    #else:
    #    return redirect('/gamelobby/pvp')
@login_required(login_url='/log_in/')
def gamestart(request,lobbyid):
    if request.method=="POST":
        lobby = Lobbies.objects.get(id=lobbyid)
        players = lobby.players.all()
        print(players)
    return redirect("/gamelobby/pvp")
# def activegame(request, room_name):
#     return render(request, 'gamelobby/pvp.html', {
#         'room_name_json': mark_safe(json.dumps(room_name)),
#         'active-room': room_name,
#     })