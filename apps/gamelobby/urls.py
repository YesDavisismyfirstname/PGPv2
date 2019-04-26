from django.conf.urls import url
from apps.gamelobby.views import gamelobby,  pvp, pvpNew, delRoom, activegame, joingame
#activegame,index

urlpatterns = [
    
    url(r'^$', gamelobby, name='lobby'),
    url(r'^pvp/(?P<room_name>[^/]+)/$', pvp, name='active'),
    url(r'^pvp/$', pvp , name='pvp'),
    url(r'pvp/join/(?P<room_name>[^/]+)/$', joingame, name="join"),
    url(r'^pvp/new$', pvpNew , name='pvpnew'),
    url(r'^pending/(?P<room_name>[^/]+)/$', activegame , name='pending'),
    url(r'^pvp/delete/(?P<room_name>[^/]+)/$', delRoom, name="delete")
]