from rest_framework import routers, serializers, viewsets

from lending.models import Lending

class LendingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lending
        fields = ('client', 'amount', 'status')
