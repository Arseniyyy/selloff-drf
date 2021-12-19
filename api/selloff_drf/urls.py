from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path('api/v1/', include('djoser.urls')),
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls.authtoken')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
