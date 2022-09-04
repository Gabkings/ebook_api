
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include("rest_framework.urls")),
    path('api/', include("ebook.urls")),
    path('api/', include("quotes.urls")),
]
