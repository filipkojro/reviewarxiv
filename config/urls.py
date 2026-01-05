from django.contrib import admin
from django.urls import path, include

from apps.reviews.views import TestView, ReviewDetailView, CommentCreateView
from apps.users.views import TestViewUsers

urlpatterns = [
    
    path("user/", TestViewUsers.as_view(), name="usersssss"),
    path("admin/", admin.site.urls),
    path("review/<int:pk>/", ReviewDetailView.as_view(), name="review_detail"),
    path("comment/create/", CommentCreateView.as_view(), name='comment_create'),
    path("", TestView.as_view(), name="test_home"),
]
