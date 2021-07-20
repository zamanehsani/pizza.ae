from django.urls import path, include
from django.views.generic import TemplateView

app_name ="dashboard"
urlpatterns = [
    path('', TemplateView.as_view(template_name="dashboard/index.html"), name="dashboard"),
]
