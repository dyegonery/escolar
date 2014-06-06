from django.conf.urls import include, url, patterns
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^notas/', include('notas.urls', namespace='notas')),
    url(r'^admin/', include(admin.site.urls)),
)