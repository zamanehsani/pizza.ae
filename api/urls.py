from django.urls import path, include, reverse_lazy
from api import views
from rest_framework import routers, viewsets
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = routers.DefaultRouter()
router.register("areas", views.AreaView)
router.register("menu-list", views.MenuView)
router.register("menu-categories", views.MenuCategoryView)
router.register("orders", views.OrderView)
router.register("profiles", views.ProfileView)
router.register("users", views.UserView)
router.register("new-order", views.NewOrderView)
router.register("customer", views.CustomerView)
urlpatterns = [
    path('', include(router.urls)),
    # token of jwt 
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # authentication
    path('api-auth', include("rest_framework.urls")),
]