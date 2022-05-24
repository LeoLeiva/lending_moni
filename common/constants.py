from decimal import Decimal
from django.utils.translation import gettext_lazy as _
from model_utils import Choices


# Some Decimal constants (to use as defaults)
DECIMAL_NAN = Decimal("NaN")  # This will be useful for hotfixes!
DECIMAL_10K = Decimal("10000.0")
DECIMAL_1K = Decimal("1000.0")
DECIMAL_HUNDRED = Decimal("100.0")
DECIMAL_HUNDRED_MIL = Decimal("100000000.0")
DECIMAL_ONE = Decimal("1.0")
DECIMAL_ZERO = Decimal("0.0")
DECIMAL_CERO_PLACES = Decimal("0")  # integer-style
DECIMAL_TWO_PLACES = Decimal("0.00")
DECIMAL_FOUR_PLACES = Decimal("0.0000")
DECIMAL_SIX_PLACES = Decimal("0.000000")
DECIMAL_EIGHT_PLACES = Decimal("0.00000000")

GENDER_MASC = "M"
GENDER_FEM = "F"
GENDER_CHOICES = Choices(
    (1, GENDER_MASC, _("Masculino")),
    (2, GENDER_FEM, _("Femenino")),
)
