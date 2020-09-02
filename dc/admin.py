from django.contrib import admin
from .models import DebitItem, CreditItem

admin.site.register(DebitItem)
admin.site.register(CreditItem)
