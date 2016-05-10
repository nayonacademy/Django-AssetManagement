from django.contrib import admin

# Register your models here.

from . models import Member,Asset,Distribution

admin.site.register(Member)
admin.site.register(Asset)
admin.site.register(Distribution)

