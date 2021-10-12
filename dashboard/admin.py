from django.contrib import admin
from dashboard import models  

admin.site.site_header = "PIZZA.AE "
admin.site.site_title = "PIZZA"
admin.site.index_title = "PIZZA Admin"


class OTP(admin.ModelAdmin):
    list_display = ( "date", 'otp', "number")
admin.site.register(models.OTP, OTP)

# list of menu category
class Menu_category(admin.ModelAdmin):
    list_display = ( 'name', 'description')
admin.site.register(models.Menu_category, Menu_category)

# menu list
class Menu(admin.ModelAdmin):
    list_display = ( "name", 'price',"new", "description", "date")
    list_filter = ("category","new")
admin.site.register(models.Menu, Menu)


# orders list 
class Order(admin.ModelAdmin):
    list_display = ( "name", 'location', "description", "date", "number", "status", "deliverer")
    list_filter = ("deliverer", "status")
admin.site.register(models.Order, Order)

class Order_item(admin.ModelAdmin):
    list_display = ('order', 'menu_item', 'quantity')
admin.site.register(models.Order_items, Order_item)

# stock list
class Stock(admin.ModelAdmin):
    list_display = ( "name", 'quantity', "unit_type", "Unit_price", "totol_price", "date", "file")
    list_filter = ("unit_type","user")
admin.site.register(models.Stock, Stock)


class About(admin.ModelAdmin):
    list_display =("name", "phone","whatsapp")
admin.site.register(models.About_company, About)

class Staff_salary(admin.ModelAdmin):
    list_display=("name", "month", "date","Pay","salary", "pay_by")
    list_filter = ("pay_by", "month")
admin.site.register(models.Staff_Salary, Staff_salary)


class Profile(admin.ModelAdmin):
    list_display = ('user', 'phone', 'address', 'about')
admin.site.register(models.Profile, Profile)

class Area(admin.ModelAdmin):
    list_display = ('id', 'name', 'min_order', 'charge')
    list_filter = ('min_order', 'charge')
admin.site.register(models.Areas, Area)

class Customer(admin.ModelAdmin):
    list_display = ("id","user", "date", "phone")
admin.site.register(models.Customer, Customer)