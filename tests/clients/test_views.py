from datetime import datetime
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.http import urlencode
import json
from datetime import timedelta
from decimal import Decimal

from rest_framework import status
from rest_framework.test import (
    APIRequestFactory,
    force_authenticate,
)
import factory
import pytest

from client.models import ClientModel
from client.views import ClientViewSet
from lending.models import Lending
from tests.factories import ClientFactory


User = get_user_model()


@pytest.mark.django_db
def test_client_list_enpoint_returns_all_active():
    """
    Test that only active clients are on the list
    """
    ClientFactory.create_batch(size=2, is_active=False)
    ClientFactory.create_batch(size=3)
    factory = APIRequestFactory()
    view = ClientViewSet.as_view({'get': 'list'})
    request = factory.get('/api/client/')
    response = view(request).render()
    active_count = ClientModel.objects.all().count()
    content = json.loads(response.content)

    assert response.status_code == status.HTTP_200_OK
    assert active_count == len(content)

@pytest.mark.django_db
def test_create_client_endpoint():
    """Test create client endpoint"""
    api_factory = APIRequestFactory()
    view = ClientViewSet.as_view({'post': 'create'})

    user = User.objects.first()

    before_lending = Lending.objects.all().count()

    request = api_factory.post(
        '/api/client/',
        {
            'first_name': 'Marco',
            'last_name': 'Van Basten',
            'gender': 1,
            'email': "marco@vanbaste.com",
            'document_number': 31234567,
            'is_active': True,
            'amount': "1200.00",
        },
        format='json'
    )
    force_authenticate(request, user=user)
    response = view(request=request)

    last_lending = Lending.objects.last()

    content = json.loads(response.render().content)
    assert response.status_code == status.HTTP_201_CREATED
    assert Lending.objects.all().count() == before_lending + 1
    assert last_lending.amount == Decimal("1200.00")
