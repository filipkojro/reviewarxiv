from django.contrib import admin
from django.urls import path, include
from apps.reviews.views import TestView

urlpatterns = [
    path("", TestView.as_view(), name="test_home"),
    path("admin/", admin.site.urls),
]
