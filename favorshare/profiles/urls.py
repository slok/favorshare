from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',


    url(r'^register/$',
        view=views.RegisterView.as_view(),
        name="register",
    ),

)
