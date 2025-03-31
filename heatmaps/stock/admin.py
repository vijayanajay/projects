from django.contrib import admin
from .models import Stock, PriceHistory


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ("symbol", "name", "sector", "is_nifty50", "updated_at")
    list_filter = ("sector", "is_nifty50")
    search_fields = ("symbol", "name")
    ordering = ("symbol",)


@admin.register(PriceHistory)
class PriceHistoryAdmin(admin.ModelAdmin):
    list_display = ("stock", "date", "open_price", "close_price", "volume")
    list_filter = ("date",)
    search_fields = ("stock__symbol", "stock__name")
    date_hierarchy = "date"
