from rest_framework import generics

from rest_framework.validators import ValidationError

from quotes.models import QuotesModel

from quotes.serializers import QuouteSerializer

from quotes.permission import IsAdminUserOrReadOnly, IsQuoteOwnerOrReadOnly

from quotes.pagination import QuotePagination


class QuotesListCreateView(generics.ListCreateAPIView):
    queryset = QuotesModel.objects.all().order_by("-id")
    serializer_class = QuouteSerializer
    permission_classes = [IsAdminUserOrReadOnly,IsQuoteOwnerOrReadOnly ]
    pagination_class = QuotePagination

    def perform_create(self, serializer):
        quote_author = self.request.user
        serializer.save(quote_author=quote_author)

class QuoteRetrieveUpdateDestryView(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuotesModel.objects.all()
    serializer_class = QuouteSerializer
    permission_classes = [IsQuoteOwnerOrReadOnly ]
    


