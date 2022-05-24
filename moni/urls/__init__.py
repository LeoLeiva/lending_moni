from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve
from rest_framework.authtoken import views

from .api_urls import urlpatterns as api_urlpatterns
from .base_urls import urlpatterns as base_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urlpatterns)),
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),
    path('', include(base_urlpatterns)),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]

# if settings.DEBUG:
#     from .dev_urls import urlpatterns as dev_urlpatterns
#     urlpatterns += dev_urlpatterns

# TODO: move this behind a view that checks for auth and permissions
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
