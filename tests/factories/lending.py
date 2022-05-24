import random
from decimal import Decimal
from factory import (
    LazyAttribute,
    LazyFunction,
    SubFactory,
)
import faker
from factory.django import DjangoModelFactory

from client.models import ClientModel
from lending.constants import LENDING_ST_STATUS_CHOICES
from lending.models import Lending

from tests.factories import ClientFactory

faker = faker.Factory.create()



def get_status_lending():
    "Return a random status choices."
    status_choices = [x[0] for x in LENDING_ST_STATUS_CHOICES]
    return random.choice(status_choices)


class LendingFactory(DjangoModelFactory):

    class Meta:
        model = Lending

    client = SubFactory(ClientFactory)
    amount = faker.pydecimal(
        positive=True,
        min_value=Decimal("1"),
        max_value=Decimal("1000"),
        right_digits=2
    )
    status = LazyFunction(lambda: get_status_lending())
