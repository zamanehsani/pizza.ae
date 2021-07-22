from django.urls import path, reverse_lazy
# from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from . import views as dashboard_views

app_name ="dashboard"
urlpatterns = [
    path('', dashboard_views.Dashboard.as_view(), name="dashboard"),
    path("menu/" ,dashboard_views.MenuList.as_view(), name="menulist"),

    # path('lockscreen', dashboard_views.Lockscreen, name='index'),
    path('login', auth_views.LoginView.as_view(template_name="dashboard/login.html"), name="login"),
    path('logout', auth_views.LogoutView.as_view(template_name="dashboard/index.html"), name="logout"),
    # password reset
    path('password-reset', 
        auth_views.PasswordResetView.as_view(template_name="dashboard/password_reset.html"), 
        name="password_reset"),

    path('password-reset-done', 
        auth_views.PasswordResetDoneView.as_view(template_name="dashboard/password_reset_done.html"), 
        name="password_reset_done"),

    path('password-reset-confirm/<uidb64>/<token>', 
        auth_views.PasswordResetConfirmView.as_view(template_name="dashboard/password_reset_confirm.html", success_url=reverse_lazy('password_has_reset')), 
        name="password_reset_confirm"),
    
    # this is view is not some how not loading. so the connfirm path with redireect to pass done function
    path('password-reset-complete', 
        auth_views.PasswordResetCompleteView.as_view(template_name="dashboard/password_complete.html"), 
        name="password_reset_complete"),
    
    # after the password redirect (this function as the password reset complete page)
    path('password-has-reset', 
        auth_views.PasswordResetDoneView.as_view(template_name="dashboard/password_complete.html"), 
        name="password_has_reset"),

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
