from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Review, Comment

# Create your views here.
class HomePageView(TemplateView):
    template_name = "reviews/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        reviews = Review.objects.all()
        context['reviews'] = reviews

        return context
    


class CommentListView(ListView):
    model = Comment
    template_name = "reviews/comment_list.html"

class CommentCreateView(CreateView):
    model = Comment
    fields = ['content', 'user', 'review', 'parent']
    template_name = "reviews/just_form.html"
    success_url = reverse_lazy('comment_list')

class ReviewListView(ListView):
    model = Review
    template_name = "reviews/review_list.html"

class ReviewCreateView(CreateView):
    model = Review
    fields = ['title', 'content', 'user', 'article_doi']
    template_name = "reviews/just_form.html"
    success_url = reverse_lazy('review_list')

class ReviewDetailView(DetailView):
    model = Review
    template_name = 'reviews/review_detail.html'
