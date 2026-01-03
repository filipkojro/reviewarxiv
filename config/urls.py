from django.contrib import admin
from django.urls import path, include

from apps.reviews.views import TestView
from apps.users.views import TestViewUsers

urlpatterns = [
    path("", TestView.as_view(), name="test_home"),
    path("user/", TestViewUsers.as_view(), name="usersssss"),
    path("admin/", admin.site.urls),
]
