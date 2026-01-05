from django.db import models

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey("users.CustomUser", on_delete=models.SET_NULL, null=True)
    article_doi = models.CharField(max_length=200)
    upvotes = models.IntegerField()
    downvotes = models.IntegerField()
    creation_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.author}"