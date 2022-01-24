from django.contrib import admin
from . models import NewStock, SoldStock

# Register your models here.
class NewStockModelAdmin(admin.ModelAdmin):
    list_display        = ["user","name", "quantity", "amount", "active", "description", "timestamp", "updated"]
    list_display_links  = ["updated", "timestamp", "user", "quantity"]
    list_editable       = ["name", "amount", "active"]
    list_filter         = ["updated", "timestamp", "description"]
    search_fields       = ["name", "description"]
    class Meta:
        model = NewStock

class SoldStockModelAdmin(admin.ModelAdmin):
    list_display        = ["user", "amount", "total_amount", "quantity","quantity_left", "stockname", "description", "timestamp", "updated"]
    list_display_links  = ["updated", "timestamp", "user", "stockname", "quantity_left"]
    list_editable       = ["quantity", "amount"]
    list_filter         = ["updated", "timestamp", "description"]
    search_fields       = ["description"]
    class Meta:
        model = SoldStock


admin.site.register(NewStock, NewStockModelAdmin)
admin.site.register(SoldStock, SoldStockModelAdmin)