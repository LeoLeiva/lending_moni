from django.db import models


class ClientModelManager(models.Manager):

    def actives(self):
        """Return clients actives."""
        return self.filter(is_active=True)

    def inactives(self):
        """Return clients inactives."""
        return self.filter(available=False)
