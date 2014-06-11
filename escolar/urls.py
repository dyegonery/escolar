from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.http import HttpResponseRedirect

urlpatterns = patterns(
    '',
    url(r'^$', lambda r : HttpResponseRedirect('notas/')),
    url(r'^notas/', include('notas.urls', namespace='notas')),
    url(r'^admin/', include(admin.site.urls)),
)