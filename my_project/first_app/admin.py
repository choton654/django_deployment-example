from django.contrib import admin
from . import models

admin.site.register(models.AccessRecord)
admin.site.register(models.WebPage)
admin.site.register(models.Topic)