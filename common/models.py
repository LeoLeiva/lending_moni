from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class BaseDatedModel(models.Model):
    """Base model with creation and edition dates."""

    created = models.DateTimeField(
        editable=False,
        verbose_name=_('Creado'),
        db_index=True,
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Actualizado')
    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        """Overwritten method to enable custom `created` value."""
        from common.utils import get_current_time
        if not self.created:
            self.created = get_current_time()
        return super().save(*args, **kwargs)
