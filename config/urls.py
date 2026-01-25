from django.contrib import admin
from django.urls import path, include

from apps.reviews.views import (
    HomePageView,
    ReviewDetailView,
    ReviewCreateView,
    ReviewUpdateView,
    ReviewListView,
    ReviewSearch,

    CommentListView,
    CommentCreateView,
    CommentDetailView,
    CommentUpdateView,
    )

from apps.users.views import TestViewUsers, UserDetailView, RegisterView

from django.contrib.auth import views as auth_views

urlpatterns = [
    
    path("users/", TestViewUsers.as_view(), name="usersssss"),
    path("admin/", admin.site.urls),

    path("reviews/", ReviewListView.as_view(), name="review_list"),
    # path("comments/", CommentListView.as_view(), name="comment_list"),
    
    path("comments/<uuid:pk>/", CommentDetailView.as_view(), name="comment_detail"),

    path("register/", RegisterView.as_view(), name='register'),
    path("login/", auth_views.LoginView.as_view(), name='login'),
    path('logged_out/', auth_views.LogoutView.as_view(), name='logout'),

    path("password_change/", auth_views.PasswordChangeView.as_view(), name='password_change'),
    path("password_change_done/", auth_views.PasswordChangeDoneView.as_view(), name="password_change_done"),

    path("", HomePageView.as_view(), name="home"),

    path("user/<str:username>/", UserDetailView.as_view(), name="user_detail"),

    path("review/<uuid:pk>/", ReviewDetailView.as_view(), name="review_detail"),
    path("review/create/", ReviewCreateView.as_view(), name='review_create'),
    path("review/<uuid:pk>/update", ReviewUpdateView.as_view(), name="review_update"),

    path("review/<uuid:review>/comment/", CommentCreateView.as_view(), name='review_comment_create'),
    path("review/<uuid:review>/<uuid:pk>/", CommentUpdateView.as_view(), name='review_comment_update'),

    path("review/search/", ReviewSearch.as_view(), name="review_search"),
]
