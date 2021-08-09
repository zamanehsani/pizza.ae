from django.urls import path, include, reverse_lazy
from api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register("areas", views.AreaView)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth', include("rest_framework.urls")),
]