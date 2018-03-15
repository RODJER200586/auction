from django.contrib import admin

from .models import Lot, Bid


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


@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'user',
        'lot',
        'amount',
        'inserted_at',
    ]
    list_filter = [
    ]
    search_fields = [
    ]
