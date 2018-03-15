from django.contrib import admin

from .models import Lot


@admin.register(Lot)
class LotAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'start',
        'finish',
        'status',
        'winner',
        'inserted_at',
        'updated_at',
    ]
    list_filter = [
        'status',
    ]
    search_fields = [
        'name',
    ]
