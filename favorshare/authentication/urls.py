from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout
#from . import views

urlpatterns = patterns('',

    url(r'^login/$',
        view=login,
        name="login",
        kwargs={'template_name': 'authentication/login.html'}
    ),

    url(r'^logout/$',
        view=logout,
        name="logout",
        kwargs={'next_page': 'homepage:index'}
    ),

)
