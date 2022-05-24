from django.utils.translation import gettext_lazy as _
from model_utils import Choices


# Lending Status Options
LENDING_ST_DRAFT = 'draft'
LENDING_ST_APPROVE = 'approve'
LENDING_ST_GRANTED = 'granted'
LENDING_ST_REJECTED = 'rejected'
LENDING_ST_AUTHORIZED = 'authorized'

LENDING_ST_STATUS_CHOICES = Choices(
    (0, LENDING_ST_DRAFT, _('Borrador')),
    (1, LENDING_ST_REJECTED, _('Rechazada')),
    (2, LENDING_ST_APPROVE, _('Aprobada')),
    (3, LENDING_ST_REJECTED, _('Autorizada')),
    (4, LENDING_ST_GRANTED, _('Otorgada')),
)
