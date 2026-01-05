from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Review

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