from rest_framework import generics
from rest_framework import mixins
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework.exceptions import ValidationError
from ebook.models import Ebook, Reviews
from ebook.serializer import EbookSerializer, ReviewsSerializer
from ebook.pagination import SimplePagination

from ebook.permissions import IsAdminUserOrReadOnly, IsReviewAuthorOrReadOnly


# class EbookListCreateAPIView(
#     mixins.ListModelMixin, 
#     mixins.CreateModelMixin,
#      generics.GenericAPIView):

#      queryset = Ebook.objects.all()
#      serializer_class = EbookSerializer

#      def get(self, request, *args, **kwargs):
#             return self.list(request, *args, **kwargs)

    
#      def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

class EbookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ebook.objects.all().order_by("-id")
    serializer_class = EbookSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = SimplePagination

class EbookDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class ReviewsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    def perform_create(self, serializer):
        ebook_pk = self.kwargs.get("ebook_pk")
        ebook = get_object_or_404(Ebook, pk=ebook_pk)
        review_author = self.request.user
        queryset = Reviews.objects.filter(ebook=ebook, review_author=review_author)
        if queryset.exists():
            raise ValidationError("You already have a reveiw")
        serializer.save(ebook=ebook, review_author=review_author)
    

class ReviewDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    permission_classes = [IsReviewAuthorOrReadOnly]
    
            

