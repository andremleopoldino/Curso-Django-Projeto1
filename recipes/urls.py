
from recipes.views import contato, home ,sobre
from django.urls import path






urlpatterns = [
    
    path('', home),
    path('sobre/', sobre),
    path('contato/', contato)
    
]