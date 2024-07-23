from django.contrib import admin
from . import models

#super user: admin (username) and admin@123 (password)

admin.site.register(models.Booking)
admin.site.register(models.Menu)
