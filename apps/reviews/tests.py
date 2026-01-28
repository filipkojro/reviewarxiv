from django.test import TestCase
from apps.users.models import CustomUser
from .models import Review

class TestEditPermissions(TestCase):
    def setUp(self):
        self.user1 = CustomUser.objects.create(username="user1", password="user1")
        self.user2 = CustomUser.objects.create(username="user2", password="user2")

        self.review1 = Review.objects.create(title="title1", content="content1", article_doi="doi1", user=self.user1)
        self.review2 = Review.objects.create(title="title2", content="content2", article_doi="doi2", user=self.user2)