from django import forms
from django.forms import ModelForm
from apps.game_window.models import Lobbies  

class newLobby(ModelForm):
    class Meta:
        model = Lobbies
        fields = ['name', 'max_players','created_by']
        
