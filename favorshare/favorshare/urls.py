from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from profiles import urls as profile_urls
from homepage import urls as homepage_urls
from authentication import urls as authentication_urls
from favors import urls as favors_urls


admin.autodiscover()

urlpatterns = patterns('',

    # Django default admin
    url(r'^admin/', include(admin.site.urls)),

    # The index of the site
    url(r'^', include(homepage_urls,
        namespace="homepage",
        app_name="homepage")
    ),

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

    # Favors
    url(r'f/', include(favors_urls,
        namespace="favors",
        app_name="favors"),
    ),


)

# Add static files (for devel env)
urlpatterns += staticfiles_urlpatterns()
