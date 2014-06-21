#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":

    settings_prefix = "favorshare.settings"

    # Get settings
    settings = {
        "staging": "staging",
        "stage": "staging",
        "sandbox": "staging",
        "production": "production",
        "prod": "production",
        "local": "local",
        "vagrant": "local",
    }

    env = os.environ['SYSTEM_ENV']

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", ".".join(
        (settings_prefix, settings.get(env, "local")))
    )

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
