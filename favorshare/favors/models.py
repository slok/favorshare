import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from django.core.validators import MaxValueValidator, MinValueValidator

from core.models import AutoDateTimeModel
from profiles.models import User


@python_2_unicode_compatible  # For Python 3.3 and 2.7
class Favor(AutoDateTimeModel):
    title = models.CharField(
        _("favor title"),
        max_length=100,
        blank=False
    )
    description = models.TextField(
        _("favor description"),
        blank=False
    )

    creator = models.ForeignKey(User, related_name="favors_i_offer")
    doer = models.ForeignKey(User, related_name="favors_i_do")

    difficulty = models.IntegerField(
        _("Difficulty of the favor"),
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10),
        ]
    )

    def __str__(self):
        return self.title


#@python_2_unicode_compatible  # For Python 3.3 and 2.7
#class Agreement(AutoDateTimeModel):
#
#    # The user that first asks for a favor (agreement creator)
#    user_a = models.ForeignKey(Favor, related_name="")
#
#    # The user that makes and offer
#    user_b = models.ForeignKey(Favor, related_name="")
#
#    # Favor owners (user_a will make user_b_favor and viceversa)
#    user_a_favor
#    user_b_favor
#
#
#    def __str__(self):
#        return self.username
#