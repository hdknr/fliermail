from django.db import models
from django.utils.translation import ugettext_lazy as _
from . import defs, methods


class MailTemplate(defs.MailTemplate, methods.MailTemplate):

    class Meta:
        verbose_name = _('Mail Template')
        verbose_name_plural = _('Mail Templates')

    def __str__(self):
        return f"{self.name} {self.subject}"