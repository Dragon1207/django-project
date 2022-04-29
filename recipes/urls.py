from django.urls import path

from recipes.views import about, contact, home

urlpatterns = [
    path('', home),
    path('contact/', contact),
    path('about/', about)
]
