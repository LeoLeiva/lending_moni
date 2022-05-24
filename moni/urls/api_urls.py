from django.contrib import admin
from django.urls import path

from client.views import ClientViewSet, ClientDetailViewSet
from lending.views import LendingViewSet

urlpatterns = [
    # path('admin/', admin.site.urls),
    path(
        'client/',
        ClientViewSet.as_view({'get': 'list'}),
        name='client'
    ),
    path(
        'client/create/',
        ClientViewSet.as_view({'post': 'create'}),
        name='client'
    ),
    path(
        'client/<int:document_number>/',
        ClientDetailViewSet.as_view({'get': 'retrieve'}),
        name='client_detail'
    ),
    path(
        'lending/',
        LendingViewSet.as_view({'get': 'list'}),
        name='lending'
    ),
]
