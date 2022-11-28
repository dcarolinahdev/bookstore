# Django
from django.urls import path
# Views
from . import views

app_name = "book"

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('book/<int:pk>/detail/', views.DetailView.as_view(), name='detail'),
]
