import random
from factory import (
    LazyAttribute,
    LazyFunction,
)
import faker
from factory.django import DjangoModelFactory

from client.models import ClientModel
from common.constants import GENDER_CHOICES

faker = faker.Factory.create()


def get_gender():
    "Return a random gender choices."
    gender_choices = [x[0] for x in GENDER_CHOICES]
    return random.choice(gender_choices)


class ClientFactory(DjangoModelFactory):
    """Client object factory."""

    class Meta:
        model = ClientModel

    first_name = LazyAttribute(lambda o: faker.first_name())
    last_name = LazyAttribute(lambda o: faker.last_name())
    gender = LazyFunction(lambda: get_gender())
    email = LazyAttribute(lambda o: faker.email())
    document_number = LazyAttribute(lambda o: faker.pyint(min_value=10000000, max_value=19999999))
    is_active = True
