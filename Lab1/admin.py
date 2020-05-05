from django.contrib import admin
from . import models

class LinkAdmin(admin.ModelAdmin):
    class Meta:
        model = models.Link

admin.site.register(models.Link, LinkAdmin)
