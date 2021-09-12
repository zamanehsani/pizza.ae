from collections import UserList
from dashboard.models import Customer, Order
from django.urls import path
# from django.views.generic import TemplateView

from . import views as dashboard_views

app_name ="dashboard"
urlpatterns = [
    path('', dashboard_views.Dashboard.as_view(), name="dashboard"),
    # profile
    path('profile/<int:pk>', dashboard_views.Profile.as_view(), name="profile"),
    path('users/', dashboard_views.UserList.as_view(), name ="users"),
    path('add-user/', dashboard_views.Add_User.as_view(), name="add_user"),
    path('user/<int:pk>/update', dashboard_views.Update_User.as_view(), name="update_user"),
    path('user/<int:pk>/delete', dashboard_views.Delete_User.as_view(), name="delete_user"),
    path('passchange/<int:pk>', dashboard_views.Passchange, name="changepss"),

    path("menu/" ,dashboard_views.MenuList.as_view(), name="menulist"),
    path("add-menu/", dashboard_views.Add_Menu.as_view(), name="add_menu" ),
    path('menu/<int:pk>/update', dashboard_views.Update_Menu.as_view(), name="update_menu"),
    path('menu/<int:pk>/delete', dashboard_views.Delete_Menu.as_view(), name="delete_menu"),

    path("add-menu-category/", dashboard_views.Add_Menu_category.as_view(), name="add_menu_category" ),
    path('menu-category/<int:pk>/update', dashboard_views.Update_Menu_category.as_view(), name="update_menu_category"),
    path('menu-category/<int:pk>/delete', dashboard_views.Delete_Menu_category.as_view(), name="delete_menu_category"),

    path("order", dashboard_views.Order.as_view(),name="order"),

    path("customer", dashboard_views.Customer.as_view(), name="customer"),
    path('add-customer/', dashboard_views.Add_Customer.as_view(), name="add_customer"),
    path('customer/<int:pk>/update', dashboard_views.Update_Customer.as_view(), name="update_customer"),
    path('customer/<int:pk>/delete', dashboard_views.Delete_Customer.as_view(), name="delete_customer"),

    path("stock/", dashboard_views.Stock.as_view(), name="stock"),
    path('add-stock/', dashboard_views.Add_Stock.as_view(), name="add_stock"),
    path('stock/<int:pk>/update', dashboard_views.Update_Stock.as_view(), name="update_stock"),
    path('stock/<int:pk>/delete', dashboard_views.Delete_Stock.as_view(), name="delete_stock"),
    # listing the urls for salary 
    path('salary', dashboard_views.Salary.as_view(), name="salary"),
    path('pay-salary', dashboard_views.Pay_salary.as_view(), name="pay_salary"),
    path('salary/<int:pk>/update', dashboard_views.Update_salary.as_view(), name="update_salary"),
    path('salary/<int:pk>/delete', dashboard_views.Delete_Salary.as_view(), name="delete_salary"),

    # area
    path('area', dashboard_views.Area.as_view(), name="area"),
    path('area/add', dashboard_views.Area_add.as_view(), name="add_area"),
    
    path('new-order', dashboard_views.New_order, name="new_order"),
]
