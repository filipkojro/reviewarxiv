from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Review, Comment

# Create your views here.
class TestView(TemplateView):
    template_name = "reviews/test.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        reviews = Review.objects.all()
        context['reviews'] = reviews

        print(reviews[0])

        return context
    
class ReviewDetailView(DetailView):
    model = Review
    template_name = 'reviews/review_detail.html'


class CommentCreateView(CreateView):
    model = Comment
    fields = ['content', 'user', 'review', 'parent']
    template_name = "reviews/comment_form.html"