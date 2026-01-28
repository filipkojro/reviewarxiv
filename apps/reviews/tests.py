from django.test import TestCase
from apps.users.models import CustomUser
from .models import Review, Comment
from django.urls import reverse


class TestPermissions(TestCase):
    def setUp(self):
        self.user1 = CustomUser.objects.create(username="user1", password="user1")
        self.user2 = CustomUser.objects.create(username="user2", password="user2")

        self.review1 = Review.objects.create(
            title="title1", content="content1", article_doi="doi1", user=self.user1
        )
        self.review2 = Review.objects.create(
            title="title2", content="content2", article_doi="doi2", user=self.user2
        )

        self.comment1 = Comment.objects.create(
            content="content1", review=self.review1, user=self.user1
        )
        self.comment2 = Comment.objects.create(
            content="content2", review=self.review2, user=self.user2
        )

    # can user edit, delete his own review / comment

    def test_user_can_edit_own_review(self):
        self.client.force_login(user=self.user1)
        responce = self.client.get(
            reverse("review_update", kwargs={"pk": self.review1.pk})
        )
        self.assertEqual(responce.status_code, 200)

    def test_user_can_edit_own_comment(self):
        self.client.force_login(user=self.user1)
        responce = self.client.get(
            reverse(
                "review_comment_update",
                kwargs={"review": self.review1.pk, "pk": self.comment1.pk},
            )
        )
        self.assertEqual(responce.status_code, 200)

    def test_user_can_delete_own_review(self):
        self.client.force_login(user=self.user1)
        responce = self.client.get(
            reverse("review_delete", kwargs={"pk": self.review1.pk})
        )
        self.assertEqual(responce.status_code, 200)

    def test_user_can_delete_own_comment(self):
        self.client.force_login(user=self.user1)
        responce = self.client.get(
            reverse("comment_delete", kwargs={"pk": self.comment1.pk})
        )
        self.assertEqual(responce.status_code, 200)

    # can user edit, delete someones review / comment

    def test_user_cant_edit_someones_review(self):
        self.client.force_login(user=self.user1)
        responce = self.client.get(
            reverse("review_update", kwargs={"pk": self.review2.pk})
        )
        self.assertEqual(responce.status_code, 403)

    def test_user_cant_edit_someones_comment(self):
        self.client.force_login(user=self.user1)
        responce = self.client.get(
            reverse(
                "review_comment_update",
                kwargs={"review": self.review2.pk, "pk": self.comment2.pk},
            )
        )
        self.assertEqual(responce.status_code, 403)

    def test_user_cant_delete_someones_review(self):
        self.client.force_login(user=self.user1)
        responce = self.client.get(
            reverse("review_delete", kwargs={"pk": self.review2.pk})
        )
        self.assertEqual(responce.status_code, 403)

    def test_user_cant_delete_someones_comment(self):
        self.client.force_login(user=self.user1)
        responce = self.client.get(
            reverse("comment_delete", kwargs={"pk": self.comment2.pk})
        )
        self.assertEqual(responce.status_code, 403)
