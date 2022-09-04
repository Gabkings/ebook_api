from rest_framework import serializers
from quotes.models import QuotesModel


class QuouteSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuotesModel
        exclude = ("quote_author",)
        # fields = "__all__"