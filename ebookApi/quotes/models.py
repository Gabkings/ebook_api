from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class QuotesModel(models.Model):
    quote_author = models.ForeignKey(User, on_delete=models.CASCADE)
    quote_body = models.TextField()
    context = models.TextField()
    source = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.quote_author}  {self.quote_body}"