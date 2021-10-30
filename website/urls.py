
from django.urls import path
from django.views.generic import TemplateView
from . import views
app_name = "website"
urlpatterns = [ 
    path('', TemplateView.as_view(template_name="website/index.html")),
    path('menu',views.Menu.as_view(), name="menu"),
    path('landing/', views.LandingPage.as_view(), name="landingpage"),
    path('customer/login/', views.LoginCustomerView.as_view(), name="customer_login"),
    path('customer/sign-up/', views.Sign_up_CustomerView.as_view(), name="customer_sign_up"),
    path('cart/', views.CartView.as_view(), name="cart_view"),
    path('order/', views.Order_cart.as_view(), name="order_cart"),
    path('order/otp', views.Order_cart_OTP.as_view(), name="order_cart_OTP"),
    path('otp-resend/', views.resend_otp, name="resend_otp"),
    path('order/address', views.Order_Location.as_view(), name="order_cart_address"),
    path('order/summary', views.Order_summary.as_view(), name="order_summary"),
    path('order/payment', views.Order_payment.as_view(), name="order_payment"),
    path('confirmed/<int:pk>', views.TrackOrder.as_view(), name="confirmed"),
    path('dine-in-menu/', views.Dine_Menu.as_view(), name="dine_menu"),
    path('dine-in-cart/', views.Dine_CartView.as_view(), name="dine_in_cart"),
    path('pizza-logo/', TemplateView.as_view(template_name="website/pizza-log.html"), name="pizza_png_log"),
    path('pizza-check/', TemplateView.as_view(template_name="website/pizza-check.html"), name="pizza_png_check"),
    path('access_token', views.Access_token, name="access_token"),
    path('order-payment-status', views.online_pay_complete, name="order_payment_status"),

]
