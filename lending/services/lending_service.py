from lending.constants import LENDING_ST_STATUS_CHOICES
from lending.models import Lending


def create_lending_with_client_id_and_amount(client, amount):
    """
    Create lending.

    @param client_id: client id from account
    @param amount: amount for lending
    """
    lending = Lending.objects.create(client=client, amount=amount, status=LENDING_ST_STATUS_CHOICES.approve)
    return lending
