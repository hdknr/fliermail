from django.db import models
from django.utils.translation import ugettext_lazy as _


class MailTemplate(models.Model):
    name = models.CharField(_('Template Name'), unique=True, max_length=50)
    sender = models.CharField(
        _('Default Sender'), max_length=100, 
        help_text=_("Name Lable <info@yourdomain.com>"))
    subject = models.CharField(_('Subjet'), max_length=200)
    body = models.TextField(_('Body'))
    is_html = models.BooleanField(_('Is HTML Mail'), default=False)

    class Meta:
        abstract = True