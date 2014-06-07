import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

from core.validators import validate_email_exists


@python_2_unicode_compatible  # For Python 3.3 and 2.7
class User(AbstractUser):
    url = models.URLField(_("user url"),
                        blank=True)
    gravatar = models.EmailField(_("gravatar email"),
                                blank=True)
    activation_token = models.CharField(
        _("activation token"),
        max_length=40,
        default=str(uuid.uuid4()),
        blank=True
    )
    reset_password_token = models.CharField(
        _("reset password token"),
        max_length=40,
        default=str(uuid.uuid4()),
        blank=True
    )

    # We could use validator explicitely when we create the attr, but this is
    # inherited from django.auth so we will add this dynamically
    def clean(self):

        # Don't do this! Get the email, can't access by key :/
        # TODO: Change toa  better way than iterating the field list
        #       (Add validation to the form only?)
        email = next((f for f in self._meta.fields if f.name == "email"))
        email.validators.append(validate_email_exists)

        super(User, self).clean()

    def __str__(self):
        return self.username
