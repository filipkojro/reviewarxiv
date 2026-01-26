from rest_framework import serializers

from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = [
            "id",
            "user",
            "title",
            "content",
            "article_doi",
            "creation_date",
            "update_date",
            "has_beed_edited",
        ]

    def get_user(self, obj):
        if obj.user:
            return obj.user.username
        return None
