from django.urls import path
from recipes.views import home, about, contact


# HTTP REQUEST <-> HTTP RESPONSE
urlpatterns = [
    path('', home),  # HOME
    path('about/', about),  # ABOUT
    path('contact/', contact),  # Contact
]