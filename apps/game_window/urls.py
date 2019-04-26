from django.conf.urls import include, url
from apps.login.views import user_list,log_in, log_out, sign_up, landing
from apps.game_window.views import gamewindow, launchgame

urlpatterns = [
    url(r'^$', gamewindow, name='lobby'),
    url(r'^room/(?P<room_id>[0-9]+)/$', launchgame, name='launch'),
]