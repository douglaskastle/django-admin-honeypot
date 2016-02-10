import django
from django.db import models
from django.utils.translation import ugettext_lazy as _
from admin_honeypot import listeners


class LoginAttempt(models.Model):
    username = models.CharField(_("username"), max_length=255, blank=True, null=True)
    if django.VERSION >= (1, 6):
        ip_address = models.GenericIPAddressField(_("ip address"), blank=True, null=True)
    else:
        # Django 1.4 and 1.5 need to have the arguments explictly populated or it doesn't work
        # in testing correctly.
        ip_address = models.GenericIPAddressField(verbose_name=_("ip address"), protocol='both', blank=True, null=True)
    session_key = models.CharField(_("session key"), max_length=50, blank=True, null=True)
    user_agent = models.TextField(_("user-agent"), blank=True, null=True)
    timestamp = models.DateTimeField(_("timestamp"), auto_now_add=True)
    path = models.TextField(_("path"), blank=True, null=True)

    class Meta:
        verbose_name = _("login attempt")
        verbose_name_plural = _("login attempts")
        ordering = ('timestamp',)

    def __str__(self):
        return self.username
