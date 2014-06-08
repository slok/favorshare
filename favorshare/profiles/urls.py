from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',

    url(r'^register/$',
        view=views.RegisterView.as_view(),
        name="register",
    ),

    url(r'^(?P<profile_id>[0-9]+)/$',
        view=views.ProfileDetailView.as_view(),
        name="detail",
    ),

    url(r'^(?P<profile_id>[0-9]+)/edit$',
        view=views.ProfileEditView.as_view(),
        name="edit",
    ),

)
