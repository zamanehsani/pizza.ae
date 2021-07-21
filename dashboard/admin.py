from django.contrib import admin
from dashboard import models  

admin.site.site_header = "PIZZA.AE "
admin.site.site_title = "PIZZA"
admin.site.index_title = "PIZZA Admin"

# list of menu category
class Menu_category(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
admin.site.register(models.Menu_category, Menu_category)

# menu list
class Menu(admin.ModelAdmin):
    list_display = ("id", "name", 'price', "description", "date")
    list_filter = ("category",)
admin.site.register(models.Menu, Menu)


# orders list 
class Order(admin.ModelAdmin):
    list_display = ("id", "name", 'location', "description", "date", "number", "status", "deliverer")
    list_filter = ("deliverer", "status")
admin.site.register(models.Order, Order)


# stock list
class Stock(admin.ModelAdmin):
    list_display = ("id", "name", 'quantity', "unit_type", "Unit_price", "totol_price", "date", "file")
    list_filter = ("unit_type","user")
admin.site.register(models.Stock, Stock)


