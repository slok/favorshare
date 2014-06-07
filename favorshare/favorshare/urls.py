from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from profiles import urls as profile_urls
from homepage import urls as homepage_urls
from authentication import urls as authentication_urls


admin.autodiscover()

urlpatterns = patterns('',

    # The index of the site
    url(r'^', include(homepage_urls,
        namespace="homepage",
        app_name="homepage")
    ),

    # Django default admin
    url(r'^admin/', include(admin.site.urls)),

    # User profiles
    url(r'p/', include(profile_urls,
        namespace="profiles",
        app_name="profiles"),
    ),

    # Authentication
    url(r'a/', include(authentication_urls,
        namespace="authentication",
        app_name="authentication"),
    ),

)

# Add static files (for devel env)
urlpatterns += staticfiles_urlpatterns()
