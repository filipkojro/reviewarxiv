from django.core.management import BaseCommand

from apps.reviews.models import Review


class Command(BaseCommand):
    def handle(self, *args, **options):
        Review.objects.create(
            title="test title",
            content="this is some content",
            author=None,
            article_doi="doi.com/kajsdfl/7162578",
            upvotes=12,
            downvotes=1,
        )
