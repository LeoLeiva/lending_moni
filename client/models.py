from django.db import models
from django.utils.translation import gettext_lazy as _

from client.managers import ClientModelManager
from common.constants import GENDER_CHOICES
from common.models import BaseDatedModel


# Create your models here.
class ClientModel(BaseDatedModel):
    """Client model for persons."""

    is_active = models.BooleanField(
        _('Activo'),
        default=True,
    )
    first_name = models.CharField(
        _("Nombre"),
        max_length=160,
        blank=True, null=True,
    )
    last_name = models.CharField(
        _("Apellido"),
        max_length=160,
        blank=True, null=True,
    )
    gender = models.SmallIntegerField(
        _("Género"),
        choices=GENDER_CHOICES,
        blank=True, null=True,
        help_text=_("Género según DNI"),
    )
    email = models.EmailField(
        _('Email'),
        blank=True, null=True,
    )
    document_number = models.CharField(
        _('Número de Doc'),
        max_length=50,
        db_index=True,
        blank=True, null=True,
    )
    objects = ClientModelManager()

    def __str__(self):
        """
        Full name object
        """
        return f"{self.first_name} {self.last_name} DNI: {self.document_number}"

    class Meta:
        verbose_name = "Prestamo"
        verbose_name_plural = "Prestamos"

    def get_full_name(self):
        return "{} {} - DNI {}".format(
            self.first_name,
            self.last_name,
            self.document_number,
        )
