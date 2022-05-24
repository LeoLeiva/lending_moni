from rest_framework import routers, serializers, viewsets

from client.models import ClientModel

# Serializers define the API representation.
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientModel
        fields = ('first_name', 'last_name', 'gender', 'email', 'document_number', 'is_active')


class ClientDetailSerializer(serializers.Serializer):
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    gender = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()
    document_number = serializers.SerializerMethodField()
    is_active = serializers.SerializerMethodField()

    class Meta:
        model = ClientModel
        fields = (
            'first_name',
            'last_name',
            'gender',
            'email',
            'document_number',
            'is_active',
        )

    def get_first_name(self, obj):
        return obj.first_name

    def get_last_name(self, obj):
        return obj.last_name

    def get_gender(self,obj):
        return obj.gender

    def get_email(self, obj):
        return obj.email

    def get_document_number(self, obj):
        return obj.document_number

    def get_is_active(self, obj):
        return obj.is_active
