from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

try:
    from django.contrib.auth import get_user_model
    User = settings.AUTH_USER_MODEL
except ImportError:
    from django.contrib.auth.models import User


class RestartRequest(models.Model):
    """
    Logs restart requests made via the admin
    """
    user = models.ForeignKey(User, editable=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('restart request')
        verbose_name_plural = _('restart requests')

    def __unicode__(self):
        return "%s - %s" % (self.user, self.created_on)
