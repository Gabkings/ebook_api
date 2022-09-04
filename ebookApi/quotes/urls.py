from django.urls import path
from quotes.views import QuotesListCreateView, QuoteRetrieveUpdateDestryView

urlpatterns = [
    path("quotes", QuotesListCreateView.as_view(), name="quotes-list"),
    path("quotes/<int:pk>", QuoteRetrieveUpdateDestryView.as_view(), name="quotes-detail"),
]