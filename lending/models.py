from django.db import models
from django.utils.translation import gettext_lazy as _

from common.constants import DECIMAL_ZERO
from common.models import BaseDatedModel
from client.models import ClientModel
from lending.constants import (
    LENDING_ST_DRAFT,
    LENDING_ST_STATUS_CHOICES,
)

# Create your models here.
class Lending(BaseDatedModel):
    """Model to represent Lending."""

    client = models.ForeignKey(
        ClientModel,
        verbose_name=_("Cliente"),
        related_name='lending_client',
        on_delete=models.CASCADE,
        null=True, blank=True,
    )

    amount = models.DecimalField(
        _("Monto solicitado del prestamo"),
        max_digits=19, decimal_places=2,
        default=DECIMAL_ZERO,
    )

    status = models.SmallIntegerField(
        _("Estado Actual del prestamo"),
        null=False, blank=False,
        choices=LENDING_ST_STATUS_CHOICES,
        default=LENDING_ST_DRAFT,
    )

    def __str__(self):
        """
        Full name object
        """
        return f"{self.client.get_full_name()}"

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
