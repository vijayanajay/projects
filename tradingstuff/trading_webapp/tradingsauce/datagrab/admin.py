from django.contrib import admin
from .models import StockSymbol

# Register your models here.
class StockSymbolAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'symbol', 'tickerNumber')
    #list_display_links = ('id', 'name', 'symbol', 'tickerNumber')
    search_fields = ('name', 'tickernumber')
    
    
admin.site.register(StockSymbol, StockSymbolAdmin)