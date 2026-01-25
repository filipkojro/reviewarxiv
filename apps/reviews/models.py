import uuid
from django.db import models
from django.conf import settings

# Create your models here.
class Review(models.Model):

    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False
    )

    title = models.CharField(max_length=200)
    article_doi = models.CharField(max_length=200)
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    
    votes_count = models.IntegerField(default=0)

    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    has_beed_edited = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} - {self.user}"
    
class ReviewVote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='votes')
    value = models.SmallIntegerField(choices=((1, 'upvote'), (-1, 'downvote')))
    
    class Meta:
        unique_together = ('user', 'review')


class Comment(models.Model):

    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False
    )

    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name="comments"
    )

    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='replies'
    )

    votes_count = models.IntegerField(default=0)

    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    has_beed_edited = models.BooleanField(default=False)

    class Meta:
        indexes = [
            models.Index(fields=['review']), # wyszukiwanie komantarzy dla konkretnej recenczji
            models.Index(fields=['review', 'creation_date']) # wyszukiwanie komantarzy dla konkretnej recenczji po dacie
        ]
        ordering = ['creation_date']

class CommentVote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='votes')
    value = models.SmallIntegerField(choices=((1, 'upvote'), (-1, 'downvote')))
    
    class Meta:
        unique_together = ('user', 'comment')