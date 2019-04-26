from django.conf.urls import url
from apps.login.views import user_list,log_in, log_out, sign_up, landing

urlpatterns = [
    url(r'^log_in/$', log_in, name='login'),
    url(r'^log_out/$', log_out, name='logout'),
    url(r'^sign_up/$', sign_up, name='register'),
    url(r'^home/$', user_list, name='user_list'),
    url(r'^$', landing, name='landing'),
    
]