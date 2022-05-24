from django.shortcuts import render
from rest_framework import status, serializers, viewsets, permissions

from lending.models import Lending
from lending.serializers import LendingSerializer

# Create your views here.
class LendingViewSet(viewsets.ModelViewSet):
    queryset = Lending.objects.all()
    serializer_class = LendingSerializer
    # permission_classes = [permissions.AllowAny]
    permission_classes = (permissions.AllowAny,)
