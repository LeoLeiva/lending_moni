import logging
from django.shortcuts import render

# Create your views here.
from rest_framework import status, serializers, viewsets, permissions
from rest_framework.response import Response

from client.models import ClientModel
from client.services.client_service import get_or_create_client_with_data, get_client_for_document_number
from client.serializers import ClientSerializer
from lending.services.lending_service import create_lending_with_client_id_and_amount

logger = logging.getLogger(__name__)


class ClientViewSet(viewsets.ModelViewSet):
    queryset = ClientModel.objects.all()
    serializer_class = ClientSerializer
    # permission_classes = [permissions.AllowAny]
    permission_classes = (permissions.AllowAny,)

    def create(self, request, *args, **kwargs):
        """
        Create a new client from submission.
        """
        data = request.data
        amount = data.get('amount')
        client = get_or_create_client_with_data(data)

        if not client:
            return Response(
                data={
                    'message': "Hubo un error al crear el cliente."
                },
                status=status.HTTP_400_BAD_REQUEST,
                content_type='application/json',
            )

        create_lending_with_client_id_and_amount(client=client, amount=amount)

        return Response(
            data={'message': "Cliente creado correctamente"},
            status=status.HTTP_201_CREATED,
            content_type='application/json',
        )


class ClientDetailViewSet(viewsets.ModelViewSet):
    """
    Client ViewSet Perfil Inversionista
    """
    serializer_class = ClientSerializer
    lookup_field = 'document_number'
    permission_classes = (permissions.AllowAny,)

    def retrieve(self, request, *args, **kwargs):
        document_number = kwargs['document_number']
        client = get_client_for_document_number(document_number)

        if not client:
            err_msg = f"No se encontró cuenta asociada al DNI {document_number}"
            logger.error(err_msg)
            return Response({"error": err_msg}, status=status.HTTP_404_NOT_FOUND)
        serializer = ClientSerializer(
            client,
        )
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        document_number = kwargs['document_number']
        client = get_client_for_document_number(document_number)

        if not client:
            err_msg = f"No se encontró cuenta asociada al DNI {document_number}"
            logger.error(err_msg)
            return Response({"error": err_msg}, status=status.HTTP_404_NOT_FOUND)
        else:
            client.delete()
        msg = f"Se borro exitosamente el usuario con DNI {document_number}"
        logger.error(msg)
        return Response({"Response": msg}, status=status.HTTP_200_OK)
