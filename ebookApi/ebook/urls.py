from django.urls import path

from ebook.views import EbookListCreateAPIView, EbookDetailApiView, ReviewDetailApiView, ReviewsListCreateAPIView

urlpatterns = [
    path('ebooks/', EbookListCreateAPIView.as_view(), name="list-ebooks"),
    path('ebooks/<int:pk>/', EbookDetailApiView.as_view(), name="detail-ebook"),
    path('ebooks/<int:ebook_pk>/review/', ReviewsListCreateAPIView.as_view(), name="list-reviews"),
    path('ebooks/<int:ebook_pk>/review/<int:pk>/', ReviewDetailApiView.as_view(), name="detail-reveiw"),
]