from django.urls import path, include
from django.views.generic import TemplateView
from django.views.generic.base import View
from . import views as dashboard_views

app_name ="dashboard"
urlpatterns = [
    path('', TemplateView.as_view(template_name="dashboard/index.html"), name="dashboard"),
    path("menu/" ,dashboard_views.MenuList.as_view(), name="menulist"),
]
