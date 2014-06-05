from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',

    url(r'^$',
        view=views.HomepageIndexView.as_view(),
        name="index",
    ),

)
