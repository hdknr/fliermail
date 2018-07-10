from django.utils.functional import cached_property
from django.core.mail.message import EmailMultiAlternatives
from email.header import Header
from email.utils import parseaddr
from fliermail.utils import render


class MailTemplate(object):

    @cached_property
    def from_header(self):
        label, address = parseaddr(self.sender)
        label = Header(label).encode('ISO-2022-JP')
        label = label.replace('\n', '')                  # newline
        return f"{label} <{address}>"

    @cached_property
    def from_address(self):
        return parseaddr(self.sender)[1]

    def create(self, destinations, from_email=None, context={}):
        subject = render(self.subject, **context)
        body = render(self.body, **context)
        mail = EmailMultiAlternatives(
            subject,
            self.is_html and strip_tags(body) or body,
            from_email=from_email or self.from_header, 
            to=destinations)
        self.is_html and mail.attach_alternative(body, "text/html")
        return mail

    def sendmail(self, recipients=[], from_email=None, dry=False, **context):
        recipients = recipients or [self.from_address]
        context = dict(entry=self)
        mail = self.create(recipients, from_email=from_email, context=context)
        if not dry:
            mail.send()
        return mail