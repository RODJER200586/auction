from django.contrib import admin

from .models import Lot


# admin.site.register(Lot)

@admin.register(Lot)
class LotAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'description',
        'image',
        'start',
        'finish',
        'status',
        'winner',
        'inserted_at',
        'updated_at',
    ]
