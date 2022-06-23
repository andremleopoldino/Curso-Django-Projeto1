

from django.urls import path
from . import views #'.' significa mesma pasta.







urlpatterns = [
    
    path('', views.home),
    path('recipes/<int:id>/', views.recipe),
    
    
]