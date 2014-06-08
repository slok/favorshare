import datetime

from django.db import models


class AutoDateTimeField(models.DateTimeField):
    """ Simple field that updates in each save """

    description = "Simple field that updates in each save"

    def pre_save(self, model_instance, add):
        return datetime.datetime.now()


# South stuff for migrations
from south.modelsinspector import add_introspection_rules
add_introspection_rules([
    (
        [AutoDateTimeField],  # Class(es) these apply to
        [],                   # Positional arguments (not used)
        {},                   # Keyword argument
    ),
], ["^core\.fields\.AutoDateTimeField"])
