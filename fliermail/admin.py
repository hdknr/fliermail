from django.contrib import admin
from fliermail import models


@admin.register(models.MailTemplate)
class MailTemplateAdmin(admin.ModelAdmin):
    list_display = [f.name for f in models.MailTemplate._meta.fields]