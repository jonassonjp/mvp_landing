from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static


# enable the admin
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'signups.views.home', name='home'),
    # url(r'^mvp_landing/', include('mvp_landing.foo.urls')),
    url(r'^thank-you/$', 'signups.views.thankyou', name='thankyou'),
    url(r'^about-us/$', 'signups.views.aboutus', name='aboutus'),
    url(r'^contact-us/$', 'signups.views.contactus', name='contactus'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                            document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                            document_root=settings.MEDIA_ROOT)

