
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
    path('track-order/<int:pk>', views.TrackOrder.as_view(), name="track_order"),
]
