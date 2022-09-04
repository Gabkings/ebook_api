from rest_framework import serializers

from ebook.models import Ebook, Reviews


class ReviewsSerializer(serializers.ModelSerializer):
    '''Reviews serializer '''

    review_author = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Reviews
        exclude = ("ebook",)
        # fields = "__all__"


class EbookSerializer(serializers.ModelSerializer):
    '''Ebook serialer model'''

    reviews = ReviewsSerializer(many=True, read_only=True)

    class Meta:
        model = Ebook
        
        fields = "__all__"

 