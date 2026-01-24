from django.contrib import admin
from django.urls import path, include

from apps.reviews.views import HomePageView, ReviewDetailView, CommentListView, CommentCreateView, ReviewCreateView, ReviewListView
from apps.users.views import TestViewUsers, UserDetailView, RegisterView

from django.contrib.auth import views as auth_views

urlpatterns = [
    
    path("users/", TestViewUsers.as_view(), name="usersssss"),
    path("admin/", admin.site.urls),

    # only for easier development, remove before deploy
    path("reviews/", ReviewListView.as_view(), name="review_list"),
    path("comments/", CommentListView.as_view(), name="comment_list"),
    path("comments/create/", CommentCreateView.as_view(), name='comment_create'),
    # path("reviews/create/", ReviewCreateView.as_view(), name='review_create'),

    path("register/", RegisterView.as_view(), name='register'),
    path("login/", auth_views.LoginView.as_view(), name='login'),
    path('logged_out/', auth_views.LogoutView.as_view(), name='logout'),

    path("", HomePageView.as_view(), name="home"),

    path("user/<str:username>/", UserDetailView.as_view(), name="user_detail"),

    path("review/<uuid:pk>/", ReviewDetailView.as_view(), name="review_detail"),
    path("review/create/", ReviewCreateView.as_view(), name='review_create'),
]
