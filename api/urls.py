from django.urls import path, include, reverse_lazy
from api import views
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = routers.DefaultRouter()
router.register("areas", views.AreaView)

urlpatterns = [
    path('', include(router.urls)),

    # token of jwt 
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # authentication
    path('api-auth', include("rest_framework.urls")),
]