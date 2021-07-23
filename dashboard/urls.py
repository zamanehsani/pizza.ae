from collections import UserList
from django.urls import path
# from django.views.generic import TemplateView

from . import views as dashboard_views

app_name ="dashboard"
urlpatterns = [
    path('', dashboard_views.Dashboard.as_view(), name="dashboard"),
    # profile
    path('profile/<int:pk>', dashboard_views.Profile.as_view(), name="profile"),
    path('users/', dashboard_views.UserList.as_view(), name ="users"),
    # path('profile/<int:pk>/u/pdate', dashboard_views.Update_profile.as_view(), name="update_profile"),

    path("menu/" ,dashboard_views.MenuList.as_view(), name="menulist"),
    path("stock/", dashboard_views.Stock.as_view(), name="stock"),
    path('add-stock/', dashboard_views.Add_Stock.as_view(), name="add_stock"),
    path('stock/<int:pk>/update', dashboard_views.Update_Stock.as_view(), name="update_stock"),
    path('stock/<int:pk>/delete', dashboard_views.Delete_Stock.as_view(), name="delete_stock"),
    # listing the urls for salary 
    path('salary', dashboard_views.Salary.as_view(), name="salary"),
    path('pay-salary', dashboard_views.Pay_salary.as_view(), name="pay_salary"),
    path('salary/<int:pk>/update', dashboard_views.Update_salary.as_view(), name="update_salary"),
    path('salary/<int:pk>/delete', dashboard_views.Delete_Salary.as_view(), name="delete_salary"),
]
