from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',

    url(r'^create/$',
        view=views.FavorCreateView.as_view(),
        name="create",
    ),

)
