from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Review, Comment

# Create your views here.
class HomePageView(TemplateView):
    template_name = "reviews/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        reviews = Review.objects.select_related("user").order_by("-creation_date")[:20]
        context['reviews'] = reviews

        return context
    


class CommentListView(ListView):
    model = Comment
    template_name = "reviews/comment_list.html"

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['content', 'user', 'review', 'parent']
    template_name = "reviews/just_form.html"
    success_url = reverse_lazy('comment_list')

class CommentDetailView(LoginRequiredMixin, DetailView):
    model = Comment
    template_name = "reviews/comment_detail.html"




class ReviewListView(ListView):
    model = Review
    template_name = "reviews/review_list.html"
    paginate_by = 2

    def get_queryset(self):
        direction = self.request.GET.get("direction", "desc")
        queryset = super().get_queryset()

        if direction == "asc":
             return queryset.order_by('creation_date')
        elif direction == "desc":
            return queryset.order_by('-creation_date')

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_direction'] = self.request.GET.get("direction", "desc")
        return context


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    fields = ['title', 'content','article_doi']
    template_name = "reviews/review_create.html"
    success_url = reverse_lazy('review_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ReviewUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Review
    fields = ['title', 'content','article_doi']
    template_name = "reviews/review_update.html"
    success_url = reverse_lazy('review_list')

    def test_func(self):
        review = self.get_object()
        return self.request.user == review.user

class ReviewDetailView(LoginRequiredMixin, DetailView):
    model = Review
    template_name = 'reviews/review_detail.html'

class ReviewSearch(TemplateView):
    template_name = "reviews/review_search.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        query = self.request.GET.get('search')
        context['query'] = query

        if query:
            reviews = Review.objects.select_related("user").filter(article_doi__icontains=query).order_by("-creation_date")[:20]
        else:
            reviews = None

        context['reviews'] = reviews

        return context