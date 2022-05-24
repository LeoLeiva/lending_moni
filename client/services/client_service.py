import logging

from client.exceptions import ClientException
from client.models import ClientModel

logger = logging.getLogger(__name__)


def get_client_for_document_number(document_number, raise_exception=False):
    client = None
    try:
        client = ClientModel.objects.get(document_number=document_number)
    except ClientModel.MultipleObjectsReturned:
        logger.error("Muchos clientes con numero de documento %s", document_number)
        if raise_exception:
            raise ClientException(f"Se encontró más de un cliente con numero de documento {document_number}")
    except ClientModel.DoesNotExist:
        logger.error("Ningun cliente con numero de documento %s", document_number)
        if raise_exception:
            raise ClientException(f"No existe el cliente con numero de documento {document_number}")
    else:
        logger.info(
            "Encontrado Cliente con numero de documento %s",
            document_number,
        )
    return client

def get_or_create_client_with_data(data):
    """
    Get or create Client instance for document_number.

    @param document_number: person's document number
    """
    document_number = data.get('document_number')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    gender = data.get('gender')
    email = data.get('email')
    client = get_client_for_document_number(document_number)
    if not client:
        logger.info("Creando Cliente con numero de documento %s", document_number)
        client = ClientModel.objects.create(
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            email=email,
            document_number=document_number,
        )
    return client
