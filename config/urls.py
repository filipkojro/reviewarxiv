from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.reviews.views import (
    HomePageView,
    ReviewDetailView,
    ReviewCreateView,
    ReviewUpdateView,
    ReviewListView,
    ReviewDeleteView,
    ReviewSearch,
    CommentCreateView,
    CommentDetailView,
    CommentUpdateView,
    CommentDeleteView,
    ReviewListAPIView,
)

from apps.users.views import UserDetailView, RegisterView

from django.contrib.auth import views as auth_views

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

APIrouter = DefaultRouter()
APIrouter.register("reviews", ReviewListAPIView, basename="review")

api_urlpatterns = [
    path("", include(APIrouter.urls)),
    # Spectacular
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("reviews/", ReviewListView.as_view(), name="review_list"),
    path("comments/<uuid:pk>/", CommentDetailView.as_view(), name="comment_detail"),
    path("comments/<uuid:pk>/confirm", CommentDeleteView.as_view(), name="comment_delete"),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logged_out/", auth_views.LogoutView.as_view(), name="logout"),
    path(
        "password_change/",
        auth_views.PasswordChangeView.as_view(),
        name="password_change",
    ),
    path(
        "password_change_done/",
        auth_views.PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    path(
        "password_reset/", auth_views.PasswordResetView.as_view(), name="password_reset"
    ),
    path(
        "password_reset_sent/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "password_reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "password_reset_done/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    path("", HomePageView.as_view(), name="home"),
    path("user/<str:username>/", UserDetailView.as_view(), name="user_detail"),
    path("review/<uuid:pk>/", ReviewDetailView.as_view(), name="review_detail"),
    path("review/create/", ReviewCreateView.as_view(), name="review_create"),
    path("review/<uuid:pk>/confirm", ReviewDeleteView.as_view(), name="review_delete"),
    path("review/<uuid:pk>/update", ReviewUpdateView.as_view(), name="review_update"),
    path(
        "review/<uuid:review>/comment/",
        CommentCreateView.as_view(),
        name="review_comment_create",
    ),
    path(
        "review/<uuid:review>/<uuid:pk>/",
        CommentUpdateView.as_view(),
        name="review_comment_update",
    ),
    path("discussion/<uuid:pk>/", CommentDetailView.as_view(), name="discussion"),
    path("review/search/", ReviewSearch.as_view(), name="review_search"),
    path("api/v1/", include(api_urlpatterns)),
]
