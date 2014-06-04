from django.conf.urls import patterns, include, url
from django.contrib import admin

from profiles import urls as profile_urls


admin.autodiscover()

urlpatterns = patterns('',

    # Django default admin
    url(r'^admin/', include(admin.site.urls)),

    # User profiles
    url(r'p/', include(profile_urls,
        namespace="profiles",
        app_name="profiles"),
    )

)
