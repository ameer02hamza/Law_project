from channels.routing import get_default_application
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LegalAid.settings")
django.setup()
application = get_default_application()