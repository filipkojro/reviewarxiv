from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from .models import Review, Comment

from rest_framework import viewsets
from .serializers import ReviewSerializer


# Create your views here.
class HomePageView(TemplateView):
    template_name = "reviews/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        reviews = Review.objects.select_related("user").order_by("-creation_date")[:20]
        context["reviews"] = reviews

        return context


class CommentListView(ListView):
    model = Comment
    template_name = "reviews/comment_list.html"


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ["content"]
    template_name = "reviews/comment_create.html"

    def form_valid(self, form):
        review_uuid = self.kwargs["review"]

        form.instance.review = get_object_or_404(Review, pk=review_uuid)

        form.instance.user = self.request.user

        return super().form_valid(form)

    def get_success_url(self):
        return reverse("review_detail", kwargs={"pk": self.kwargs["review"]})


class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    fields = ["content"]
    template_name = "reviews/comment_create.html"

    def get_success_url(self):
        return reverse("review_detail", kwargs={"pk": self.kwargs["review"]})

    def form_valid(self, form):
        form.instance.has_beed_edited = True
        return super().form_valid(form)


class CommentDetailView(LoginRequiredMixin, DetailView):
    model = Comment
    template_name = "reviews/comment_detail.html"


class ReviewListView(ListView):
    model = Review
    template_name = "reviews/review_list.html"
    paginate_by = 50

    def get_queryset(self):
        return super().get_queryset().order_by("-creation_date")


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    fields = ["title", "content", "article_doi"]
    template_name = "reviews/review_create.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    fields = ["title", "content", "article_doi"]
    template_name = "reviews/review_update.html"
    success_url = reverse_lazy("home")

    def test_func(self):
        review = self.get_object()
        return self.request.user == review.user

    def form_valid(self, form):
        form.instance.has_beed_edited = True

        return super().form_valid(form)


class ReviewDetailView(LoginRequiredMixin, DetailView):
    model = Review
    template_name = "reviews/review_detail.html"

    def get_queryset(self):
        return super().get_queryset().prefetch_related("comments")


class ReviewSearch(TemplateView):
    template_name = "reviews/review_search.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        query = self.request.GET.get("search")
        context["query"] = query

        if query:
            reviews = (
                Review.objects.select_related("user")
                .filter(article_doi__icontains=query)
                .order_by("-creation_date")[:20]
            )
        else:
            reviews = None

        context["reviews"] = reviews

        return context


class ReviewListAPIView(viewsets.ModelViewSet):
    """
    List of reviews from RevewArxiv
    """

    serializer_class = ReviewSerializer
    queryset = Review.objects.all().select_related("user")
